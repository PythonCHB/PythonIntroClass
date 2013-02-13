import isi.app.lib.procs as procs
import isi.hw.hal as hal
import isi.hw.version as hwver

import isi.hw.check.lib.filenames as files
import isi.hw.check.lib.log as loglib
import isi.hw.check.lib.misc as misc
import isi.hw.check.lib.nvram as nvram
import isi.hw.check.lib.ramdisk as ramdisk
import isi.hw.check.lib.syslog as sysloglib


# jcc start
import sys
import signal
import time
import isi.hw.check.mfg.consts as consts
start_time = time.time()
abs_starttime = start_time
consts_nvramscrub   = consts.nvramscrub_target_run_time()['long']    # jcc
#import pdb; pdb.set_trace()   #jcc
target_run_time = int ( consts_nvramscrub['target_run_time'] )     # jcc
# jcc end


pass_str = 'nvram scrub passed'

default_reps = 10

# maxtime?

def run(reps = None, sections = 125, checkpoint = 0):
    log = loglib.get_logger()
    ramdir = ramdisk.disk_dir()
    nvramdev = hal.getNvramDevicePath()
    randfile = '/dev/random'

    blocksize = 1024 * 1024 # see dd cmd, bs=1024k
    nvramsize = nvram.get_nvram_size()
    expd_nvramsizes = nvram.get_nvram_sizes()

    if not nvramdev:
        log.fail("No nvram device available for test", 0)
        return
    if not expd_nvramsizes:
        log.fail("No official nvram specs for hardware family '%s'" %
                 hwver.hwgenName(hwver.hwgen), 0)
        return

    # Validate or prompt for reps
    if reps != None:
        try:
            reps = int(reps)
            if reps <= 0:
                raise ValueError()
        except ValueError:
            log.fail('Invalid reps parameter (%s)' % reps)
            return # hard fail
    else:
        while 1:
            reps = log.prompt('Iteration count (%d): ' %
                                     default_reps)
            if reps == '':
                reps = default_reps
            try:
                reps = int(reps)
                if reps <= 0:
                    raise ValueError()
                log.out('')
                break
            except ValueError:
                log.out('Invalid iteration count; please enter a positive ' +
                        'integer')                

    # Init the ram disk (moved from isi_mfg_check script)
    # XXX This ramdisk lib is crap, and needs serious attention
    ramdisk.init()
    log.out('')

    # clear ECC counts to 0 before test
    if nvram.pre_test_clear_ecc_errors():
        return # hard fail

    log.out('')

    # Open the nvram log file for appending. After writing to it, be
    # sure to flush it before any calls to 'echo xyz >> loglib.nvram_log()',
    # otherwise output can get out of sync.
    try:
        nvramlog = open(loglib.nvram_log(), 'a')
    except IOError:
        log.fail('Unable to open nvram log file for appending: %s' %
                 loglib.nvram_log(), 0)
        return # hard fail

    def nvramlogwrite(output):
        if isinstance(output, basestring):
            output = [output]
        for out in output:
            nvramlog.write("%s\n" % out)
            nvramlog.flush()

    def testString(iter, sec=None):
        test = "Test %d of %d" % (iter+1, reps)
        if not sec is None:
            test += ": sec %d:" % (sec)
        return test

    def ddexec(iter, sec, ddcmd):
        cmd = 'dd if=%s of=%s bs=1024k count=4' % (ddcmd['if'], ddcmd['of'])
        if ddcmd['option']:
            cmd += ' %s' % ddcmd['option']
        # Note previously this cmd was piped: 1>/dev/null 2>/dev/null
        (error, output) = procs.get_cmd_output(cmd)
        try:
            outerr = output[0]
        except:
            outerr = ''
        if error:
            out_str = ('%s: dd from %s to %s failed: %s' %
                       (testString(iter,sec), ddcmd['src'], ddcmd['dest'],
                        outerr))
            log.fail(out_str, 0)
            # Push dd output to logfile
            output.insert(0, out_str)
            nvramlogwrite(output)
        return error

    def checkjournal(iter, start=True):
        # Uses: nvramlog, log, reps, checkpoint
        error = 0
        if iter >= checkpoint or iter == -1:
            if iter == -1:
                test = 'Pre-Test'
                out_str = ('%s -- checking journal' % test)
            else:
                test = testString(iter)
                out_str = ('%s -- checking journal (%s)' %
                           (test, start and "start" or "end"))
            log.out(out_str)
            nvramlogwrite(out_str)
            cmd = files.commands['checkjournal']
            def echo_func(x):
                nvramlog.write('%s\n' % x)
                nvramlog.flush()
            (error, output) = procs.proc_cmd_output(cmd, echo_func)
            nvramlog.flush()
            if not error:
                volt_fails = nvram.extract_voltage_failures(output)
            if error or volt_fails:
                error = 1
                out_str = '%s: Journal check failed' % test
                #procs.get_cmd_output('echo %s >> %s' %
                #                     (out_str, loglib.nvram_log()))
                #nvramlog.flush()
                nvramlogwrite(out_str)
                log.fail('%s; see %s file for details' %
                         (out_str, loglib.nvram_log()), 0)
        return error

    nvramlogwrite([
        "nvramscrub: reps=%s, sections=%s, checkpoint=%s" %
        (reps, sections, checkpoint),
        "nvramscrub: ramdir=%s nvramdev=%s randfile=%s" %
        (ramdir, nvramdev, randfile),
        "",
        ])
        
    fail_count = 0

    # Tag the syslog with a marker to wrap the test; used for
    # extract_syslog_entries reporting, see end of test.
    syslog_marker = sysloglib.init_syslog_marker('nvramscrub')

    # Do an initial sanity checkjournal, first
    if checkjournal(iter=-1):
        fail_count += 1
        log.fail('Pre-Test NVRAM checkjournal errors detected', 0)
        log.out('')

    # We have a protection limit on dd offsets to prevent dd errors:
    #  /dev/mnv0: end of device
    # We rely on reported nvram size from hwver; This is checked
    # independently by safe.id.nvram, but go ahead and report a failure here
    # (once!) if testing would exceed this limit AND reported size mismatch
    # the expected safe.id.nvram values.
    out_str = 'Pre-Test -- checking NVRAM size limits'
    log.out(out_str)
    nvramlogwrite(out_str)
    # max(s in sections loop) = sections-1, but r=s+1, so max(r)=sections
    start_max = blocksize * (sections*4)
    if start_max >= nvramsize:
        # If reported nvramsize is less than expected, report failure
        if start_max < min(expd_nvramsizes):
            out_strs = ['- Unable to test at max dd skip offset %dB:' %
                        start_max,
                        '- Detected NVRAM size %dB, Expected %s' %
                        (nvramsize, misc.should_be(map(lambda s: '%dB' % s,
                                                       expd_nvramsizes)))]
            for out_str in out_strs:
                log.fail(out_str, 0)
                nvramlogwrite(out_str)
            fail_count += 1

    abs_starttime = time.time()   #jcc

    # Run the test loop
    log.out('[nvramscrub] start: target_run_time=%s seconds' % ( target_run_time ))
    #print "jcc nvramscrub: start_time   '" + str( time.time() ) + "' seconds"
    for i in range(reps):
        failed = False
        r = 0
        log.out('%s -- scrubbing journal' % testString(i))

	# jcc start
	time_now    = time.time() - abs_starttime
	time_remain = target_run_time - time_now
	if ( time_now < target_run_time ):
		# #print "jcc lcdscrub: remaining_time '" + str( time_remain ) + "' seconds"
	        pass
	else:
		log.out('[nvramsrub] end: target_run_time=%s seconds is reached, exited' % (target_run_time))
		if fail_count > 0:
			log.fail('Test failed')
	        else:
			log.out('All tests succeeded')
	        return

        if checkjournal(i, start=True):
            failed = True

        for s in range(sections):
            r += 1
            start = blocksize * (r*4)
            if start >= nvramsize:
                # Don't dd, will get error: /dev/mnv0: end of device
                continue
                    
            writefile = '%s/randfilewrite%d%d' % (ramdir, i, s)
            readfile = '%s/randfileread%d%d' % (ramdir, i, s)

            ddcommands = [
                { 'src': randfile, 'dest': 'ramdisk',
                  'if': randfile, 'of': writefile, 'option': None,
                  },
                { 'src': 'ramdisk', 'dest': 'nvram',
                  'if': writefile, 'of': nvramdev, 'option': "seek=%d" % (r*4),
                  },
                { 'src': 'nvram', 'dest': 'ramdisk',
                  'if': nvramdev, 'of': readfile, 'option': "skip=%d" % (r*4),
                  },
                ]
            for ddcmd in ddcommands:
                error = ddexec(i, s, ddcmd)
                if error:
                    failed = True
                    break

            # Compare results, if successful dd's above
            if not error:
                cmd = 'diff %s %s' % (readfile, writefile)
                (error, output) = procs.get_cmd_output(cmd)
                if error:
                    failed = True
                    out_str = '%s: dd result diff failed:' % testString(i,s)
                    log.fail(out_str, 0)
                    # Push failure message to logfile
                    nvramlogwrite(out_str)
            
            # Cleanup ramdisk - Always
            procs.get_cmd_output('rm -f %s %s 1> /dev/null 2> /dev/null' %
                                 (readfile, writefile))

        if checkjournal(i, start=False):
            failed = True

        if failed:
            fail_count += 1

    if fail_count > 0:
        log.fail('%d of %d tests failed' % (fail_count, reps), 0)

    # Check NVRAM for ECC errors
    if nvram.post_test_check_ecc_errors():
        fail_count += 1

    # Check syslog for NVRAM ECC errors
    if nvram.check_nvram_syslog_errors(marker=syslog_marker):
        fail_count += 1
    log.out('')

    if fail_count > 0:
        log.fail('Test failed')
    else:
        log.out('All tests succeeded')
