#!/usr/bin/env python

# TO DO:
# - Add storage so that data can be stored in a shelve db so the file system does not
# need to be scanned each time. :: IN Duper.py
# - Add ability to store meta data in shelve along with file path. In future code
# could be written that uses this data to create a samples db... :: IN Duper.py
# - Add use of opt parser. :: DONE
# - Add option for re-scan. if not, it should use the shelve db. If no db exists,
# do scan. :: IN Duper.py :: May add here too...


import hashlib
import os
import time
import threading
from optparse import OptionParser

VERSION = "0.3"


class DupeChecker(object):
    def __init__(self):
        self.supported_types = ('aif', 'aiff', 'wav', 'mp3', 'aac', 'm4a')
        self.master_dict = {}
        self.base_path = ''
        self.ext_limit = []
        self.pre_list = []
        self.checker = None

    def pre_scan(self, in_path, in_exts=['wav', 'aif', 'aiff']):
        self.pre_list = []
        self.base_path = os.path.abspath(in_path)
        allowed_exts = [ext for ext in in_exts if ext in self.supported_types]
        for root, dirs, files in os.walk(self.base_path):
            for f in files:
                ext = ''
                try:
                    # splitext returns '.ext' for second arg, [1:] is 'ext'
                    ext = os.path.splitext(f)[1][1:]
                    if ext in allowed_exts:
                        self.pre_list.append(os.path.join(root, f))
                except Exception:
                    pass  # Don't care if it fails, most likely cause is file has no extension
                    # and we wouldn't know the type anyway, no magic type discovery...
        return len(self.pre_list)

    def do_scan(self):
        self.checker = Checker(self.pre_list)
        print "Started..."
        self.checker.start()

    def update(self):
        if self.checker.is_alive():
            return self.checker.get_processed_count()
        return len(self.pre_list)

    def get_data(self):
        if not self.checker.is_alive():
            return self.checker.get_data()

    def do_shutdown(self):
        self.checker.shutdown()


class Checker(threading.Thread):
    def __init__(self, file_list):
        threading.Thread.__init__(self)
        self.file_list = file_list
        self.dupe_dict = {}
        self.tmp_keys_dict = {}
        self.count = 0
        self.do_go = True

    def run(self):
        self.count = 0
        for _file in self.file_list:
            if not self.do_go:
                break
            _hash = self.do_file_hash(_file)
            if (_hash):
                self.do_process_hash(_hash, _file)
            self.count += 1
            if self.count % 5 == 0:
                # Be nice
                time.sleep(.1)

    def do_file_hash(self, inPathName):
        sha1Obj = hashlib.sha1()
        fHandle = open(os.path.abspath(inPathName), 'rb')
        if (fHandle):
            for chunk in iter(lambda: fHandle.read(128 * sha1Obj.block_size), ''):
                sha1Obj.update(chunk)
        return sha1Obj.hexdigest()

    def do_process_hash(self, inHash, inPath):
        if (inHash in self.tmp_keys_dict):
            if (inHash in self.dupe_dict):
                self.dupe_dict[inHash].append(inPath)
            else:
                self.dupe_dict[inHash] = []
                self.dupe_dict[inHash].append(self.tmp_keys_dict[inHash])
                self.dupe_dict[inHash].append(inPath)
        else:
            self.tmp_keys_dict[inHash] = inPath

    def shutdown(self):
        self.do_go = False

    def get_processed_count(self):
        return self.count

    def get_data(self):
        return self.dupe_dict


def do_cli_opts():
    parser = OptionParser(version=VERSION)
    parser.add_option('-b', '--base_path', dest='basepath', default='/',
        action='store', type='string', help="Base path to start file check.")
    parser.add_option('-f', '--output_file', dest='outfile', default='./dupe_data.txt',
        action='store', type='string', help="File to write dupe data to. If not used, data will print to stdout.")
    parser.add_option('-e', '--ext', help="List of file extensions, comma separated.",
        action='store', type='string', dest='exttype', default='aif,aiff,wav')
    # Not supported yet... in cli version
    # scanHelp = "Rescan system and rebuild dupe cache. Note: if running for the first time it will always do a scan."
    # parser.add_option('-r', '--rescan', dest='rescan', action='store_true',
    #    default=False, help=scanHelp)
    parser.add_option('-v', '--verbose', dest='verbose', action='store_true',
        default=False, help="Print extra output to stdout.")
    parser.add_option('-d', '--debug', dest='debug', action='store_true',
        default=False, help="Print debug messages to stdout.")
    return parser.parse_args()


def write_data(file_path, data):
    fh = open(file_path, 'w')
    for key in data:
        fh.write(str(key) + '\n')
        for f in data[key]:
            fh.write(str(f) + '\n')
    fh.close()

if (__name__ == "__main__"):
    opts, args = do_cli_opts()
    basePath = opts.basepath
    fileOut = opts.outfile
    extType = opts.exttype
    runner = DupeChecker()
    total = runner.pre_scan(basePath, fileOut, extType)
    processed = 0
    while processed < total:
        processed = runner.update()
    data = runner.get_data()
    write_data('dupe_checker_matches.txt', data)
