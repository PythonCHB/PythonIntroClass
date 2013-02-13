#!/usr/bin/python -u
# Scott Aylward

"""
treegen is a tool for generating directory trees and test files.

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -d DEPTH, --depth=DEPTH
                        Tree depth
  -w WIDTH, --width=WIDTH
                        Directory width
  -f SIZE, --files=SIZE
                        Make files of specified size at lowest level. Size in
                        bytes unless K, M, or G is specified.
  -s, --sparse          Create sparse files instead of filling them with random bits.
  -p PATH, --path=PATH  Target path. Defaults to cwd.
  -t, --time			Time tree generation. Useful for perf testing.
  --ext=EXT             Adds an extension to each created file.
  --pre=PREFIX          Adds prefix to directory names.
Example usage: 

treegen -d 4 -w 10 -f 10K -p /home/foo/test -s
treegen -d 0 -w 100 -f 1G
treegen -d 5 -w 3 -f 0 --ext=.jpg
treegen -d 4 -w 16 --pre=dirname -t
treegen -d 2 -w 5 -p ./testdata 
"""

desc="%prog is a tool for generating directory trees and test files."
ver="%prog version 0.9c"
use="%prog -d <depth> -w <width> [option]"
exs="""Example usage: \n
treegen -d 4 -w 10 -f 10K -p /home/foo/test -s
treegen -d 0 -w 100 -f 1G
treegen -d 5 -w 3 -f 0 --ext=.jpg
treegen -d 4 -w 16 --pre=dirname -t
treegen -d 2 -w 5 -p ./testdata \n
"""

import os, errno, sys

class TreeGen():
    def __init__(self, depth, width, fsize=None, fsparse=False, ext=None, pre=None):
        """Initializes class vars and runs the primary methods. Takes tree depth and width as minimum arguments.
        Complete args are depth, width, file size, use sparse files(bool), file extension, directory prefix."""
        self.depth = depth
        self.width = width
        self.fsize = fsize
        self.fsparse = fsparse
        self.ext = ext
        self.pre = pre
        if self.fsize is not None:
            self.realsize = self.convert()
        self.dirtree(depth, 0, width)
        self.treecalc(depth, width)

    def create_dir(self, t_num):
        """Creates one directory per iteration in the dirtree function"""
        # add directory prefix if given
        if self.pre is None:
            target = str(t_num)
        else:
            target = self.pre + str(t_num)
        # Now with error handling!
        try:
            os.mkdir(target)
        except OSError as exc:
            if exc.errno == errno.EEXIST:
                if os.path.isfile(target):
                    os.unlink(target)
                    os.mkdir(target)
                else:
                    pass
            else: raise
        os.chdir(target)

    def create_file(self, t_num):
        """Creates one file per iteration in the dirtree function"""
        # add file extension if given
        if self.ext is None:
            target = str(t_num)
        else:
            target = str(t_num) + self.ext
        # make files of provided size
        try:
            if self.fsize is not None:
                f = open(target, 'wb')
                if self.fsize is not '0':
                    if self.fsparse is False:
                        #memory errors on urandom calls around 1GB or bigger, so taking 1M chunks
                        if self.realsize < 1048576:
                            f.write(os.urandom(self.realsize))
                        else:
                            for chunks in xrange(self.realsize / 1048576):
                                f.write(os.urandom(1048576))
                    else:
                        f.seek(self.realsize - 1)
                        f.write('\0')
                f.close()
        except OSError as exc:
            if exc.errno == errno.EEXIST:
                pass
            else: raise	

    def dirtree(self, d_max, d_cur, w_max):
        """Create the requested directory structure. 
        d_cur should always be passed to the function initially as 0 and increments when it recurses.
        d_max and w_max should be integers representing desired tree depth and width, respectively.
        """
        count = 0
        while count < w_max:
            if d_cur < d_max:
                self.create_dir(count)
                # function recurses here with an interation of the current depth
                self.dirtree(d_max, d_cur + 1, w_max)
                os.chdir("..")
            else:
                self.create_file(count)
            count += 1

    def convert(self):
        """Take human-readable file size(fsize as str) and return as bytes(number as int)"""
        lookup = {'K': 1024, 'M': 1048576, 'G': 1073741824}
        unit = self.fsize[-1]
        unit = unit.upper()
        try:
            if unit in lookup:
                number = int(self.fsize[:-1])
                return lookup[unit] * number
            else:
                number = int(self.fsize)
                return number
        except ValueError:
            print "%s is not a valid file size. Please specify size in the form of <int>[K/M/G]." % fsize
            sys.exit()

    def treecalc(self, d_max, w_max):
        """Accepts two integers representing the depth(d_max) and width(w_max) of a tree
        and prints the number of directories and files at each level, 
        as created with the dirtree function"""
        d_cur = 1
        while d_cur <= (d_max + 1):
            numdirs = (w_max**d_cur)
            if d_cur <= d_max:
                print "Level %d directories: %d" % (d_cur, numdirs)
            else:
                if self.fsize is not None:
                    print "Level %d files: %d" % (d_cur, numdirs)
            d_cur += 1

if __name__ == "__main__":
    import optparse, time
    class CLI():
        def main(self):
            """Handle command arguments with optparse(for pre-2.7 compatibility) and run the other functions"""
            # optparse strips newlines with default formatting, so override that here
            optparse.OptionParser.format_epilog = lambda self, formatter: self.epilog

            p = optparse.OptionParser(description=desc,
                                            version=ver,
                                            usage=use,
                                            epilog=exs)
            p.add_option("--depth", "-d", dest="depth", type="int", help="Tree depth")
            p.add_option("--width", "-w", dest="width", type="int", help="Directory width")
            p.add_option("--files", "-f", dest="size", type="string", help="Make files of specified size at lowest level. Size in bytes unless K, M, or G is specified.")
            p.add_option("--sparse", "-s", dest="sparse", action="store_true", help="Create sparse files instead of filling them with data.",  default=False)
            p.add_option("--path", "-p", dest="path", help="Target path. Defaults to cwd.", default=os.getcwd())
            p.add_option("--time", "-t", dest="time", action="store_true", help="Time tree generation. Use for perf testing.", default=False)
            p.add_option("--ext", dest="ext", help="Adds an extension to each created file.")
            p.add_option("--pre", dest="prefix", help="Adds prefix to directory names.")

            options, args = p.parse_args()

            if options.depth and options.width:
                try:
                    os.chdir(options.path)
                except OSError as exc:
                    if exc.errno == errno.ENOENT:
                        os.makedirs(options.path)
                        os.chdir(options.path)
                    else: raise
                start = time.time()
                TreeGen(options.depth, options.width, options.size, options.sparse, options.ext, options.prefix)
                end = (time.time() - start)
                if options.time:
                    print "Tree created in %i seconds" % end
            else:
                print "**Tree depth and width arguments are required.**\n"
                p.print_help()

        def run(self):
            try:
                self.main()
            except KeyboardInterrupt:
                print "\nInterrupted"
                sys.exit()

    CLI().run()
