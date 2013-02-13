#!/usr/bin/env python
# vim: ts=4 sw=4 softtabstop=4 expandtab autoindent

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import cPickle as pickle
import re
import pprint

"""
This python scripts parses isi_mfg_check output_log files that
are created during Nodeburn to try to determine how long each
subtest ran.
"""

class REGMatch:
    """ Keeps regex group intact """
    def __or__(self, value):
        'save value as _ and return value'
        self._ = value
        return value

    def group(self, grp=0):
        'return _.group(grp)'
        return self._.group(grp)

def fix_timestamp(testdata, hms, nbstart=None):

    # Incoming 24-hour timestamp missing MM/DD/YYYY
    # e.g. hms = 23:43:24

    # lhms e.g. ['23', '43', '24']
    lhms = hms.split(':')
    
    # Change our refernce time depending on whether this func is
    # being called for the first time
    if ( nbstart == True ):
        mark = 'logstart'
    else:
        mark = 'nbindex'
    # Pulling MM/DD/YYYY and HH:MM:SS from either the beginning of the
    # log file or the previous timestamp
    mdmy = testdata[mark].strftime('%m/%d/%y').split('/')
    mhms = testdata[mark].strftime('%H:%M:%S').split(':')

    # Add a day to MM/DD/YYYY if HH:MM:SS rolls over
    if ( lhms < mhms ):
        temp = testdata[mark] + relativedelta(days=+1)
        dmy = temp.strftime('%m/%d/%y')
    elif ( lhms >= mhms ):
        dmy = testdata[mark].strftime('%m/%d/%y')

    # Return new timestamp that includes MM/DD/YYYY
    testdata['nbindex'] = parse( dmy + " " + hms )
    return testdata['nbindex']

def main():

    pp = pprint.PrettyPrinter(indent=4)

    fparse = open('sample.txt', 'r')

    testdata = {}
    diskscrub = {}
    drive_count = 0
    tests = ['diskscrub','nvramscrub','lcdscrub','net']
    nodeburn_lines = 0

    #e.g. : (Wed May 23 23:09:24 2012)
    sregx_ols = r'^\s+: (\w{3} [JFMASOND]\w+ \d+ \d\d:\d\d:\d\d \d{4})$'
    rregx_ols = re.compile(sregx_ols)

    #e.g. : Nodeburn config number     = (400-0029-01)
    sregx_chassisconf = r': Nodeburn config.*= (\S+)$'
    rregx_chassisconf = re.compile(sregx_chassisconf)

    #e.g. : Nodeburn serial number     = (SX400-301220-0146)
    sregx_serialnum = r': Nodeburn serial.*= (\S+)$'
    rregx_serialnum = re.compile(sregx_serialnum)

    # e.g. : Build                         = (B_6_5_5_7_MFG_21(RELEASE))
    sregx_build = r': Build\s+=\s(\S+)$'
    rregx_build = re.compile(sregx_build)

    # e.g. : Bay 36 - Hitachi HUA723020ALA640 FW:MK7OA8P0 (3907029168 bl...
    sregx_drive = r': Bay (\d+)\s+- \S+ \S+.*SN:\S+$'
    rregx_drive = re.compile(sregx_drive)

    # e.g. [HH:MM:SS]
    sregx_nburn = r'\[(\d\d:\d\d:\d\d)\](.*$)'
    rregx_nburn = re.compile(sregx_nburn)

    mreg = REGMatch()

    while 1:

        lines = fparse.readlines()

        if not lines:
            break
        
        for linenum, line in enumerate(lines):

            #e.g. : (Wed May 23 23:09:24 2012)
            if mreg|rregx_ols.search(line):
                testdata['logstart'] = parse(mreg.group(1))

            #e.g. : Nodeburn serial number = (SX400-301220-0146)
            if mreg|rregx_serialnum.search(line):
                testdata['serial'] = mreg.group(1).lstrip()
            
            #e.g. : Nodeburn config number\s+= (400-0029-01)
            if mreg|rregx_chassisconf.search(line):
                testdata['config'] = mreg.group(1).lstrip()

            # e.g. : Build\s+= (B_6_5_5_7_MFG_21(RELEASE))
            if mreg|rregx_build.search(line):
                testdata['build'] = mreg.group(1).lstrip()

            # e.g. : Bay 36 - Hitachi HUA723020ALA640 FW:MK7OA8P0 (390702...
            if mreg|rregx_drive.search(line):
                drive = {}
                drive_count += 1
                
                # Get drive bay
                bay = str(mreg.group(1))
                drive['bay'] = bay
                
                # Get drive model
                model = re.search(r'-(.*)FW:', line)
                drive['model'] = model.group(1).lstrip().rstrip()

                # Get drive firmware
                firmware = re.search(r'FW:(\S+)\S+', line)
                drive['firmware'] = firmware.group(1)

                # Get drive blocks
                blocks = re.search(r'\((\d+) blks\)', line)
                drive['blocks'] = blocks.group(1)

                # Get drive serial number
                serial = re.search(r'SN:(\S+)', line)
                drive['serial'] = serial.group(1)

                # Add info to data dictionary
                diskscrub['drive_' + bay] = drive
                
            # e.g. [00:00:00]
            if mreg|rregx_nburn.search(line):
                nodeburn_lines += 1
                timestamp = mreg.group(1)

                """ There are five subtests in nodeburn:
                    - memscrub
                    - diskscrub
                    - nvramscrub
                    - lcdscrub
                    - net """

                # Start of mfg.long.memscrub
                if re.search('mfg.long.memscrub', line):
                    newstamp = fix_timestamp(testdata, timestamp, nbstart=True)
                    testdata['nodeburn'] = [newstamp]
                
                # memscrub lines don't have [memscrub] in them...
                if re.search('[Fixed|Random]\s+Iteration.*MB/s', line):
                    newstamp = fix_timestamp(testdata, timestamp)
                    try:
                        testdata['memscrub'][1] = newstamp
                    except KeyError:
                        testdata['memscrub'] = [newstamp, newstamp]
                    except:
                        print "Unexpected error determining duration of: memscrub"
                
                # Parse lines [diskscrub], [nvramscrub], [lcdscrub], [net]
                for test in tests:
                    if re.search('\[' + test, line):
                        newstamp = fix_timestamp(testdata, timestamp)
                        try:
                            testdata[test][1] = newstamp
                        except KeyError:
                            testdata[test] = [newstamp, newstamp]
                        except:
                            print "Unexpected error determining duration of:", test
    
    fparse.close()
    
    testdata['drive_count'] = drive_count
    testdata['nodeburn_lines'] = nodeburn_lines
    testdata['nodeburn'].append(testdata['nbindex'])
    tests.append('memscrub')
    tests.append('nodeburn')
    for test in tests:
        print "Duration of %s: %s" % (test, testdata[test][1] - testdata[test][0])

    #pp.pprint(testdata)
    #pp.pprint(diskscrub)

if __name__ == "__main__":
    main()
