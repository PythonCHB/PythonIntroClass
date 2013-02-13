#TODO:
# make a list of clones and pick one to write
# add optparse, for "run forever" and "prefix"
# pick a realistic seek for the write

import random
import subprocess
import sys
import time

debug = False
#debug = True
clones = { }
clone_key = 1
loop_num = 100000

def make_file(srcpath="/ifs/data/source",filename="a"):
    blocksize=256
    count=10
    # Make the directory
    # Should prolly make this conditional on if dir already exists
    string_e = "mkdir -p %s"%(srcpath)
    exec_string(string_e)

    # Make the file
    string_a = "qadd -q bs=%dM count=%d of=%s/%s oflag=sync"%(blocksize,
               count,srcpath,filename)
    exec_string(string_a)

class Clone(object):
    def __init__(self,host,snapname,srcpath,filename,clonepath,uniq):
        self.host = host
        self.snapname = snapname
        self.srcpath = srcpath
        self.filename = filename
        self.clonepath = clonepath
        self.uniq = uniq
        self.clonefile = "%s/%s_clone_%s"%(self.clonepath,self.filename,self.uniq)

    def make(self):
        # Take a snapshot
        string_a = "isi snapshot snapshot create --name %s --path %s"%(self.snapname, self.srcpath)
        exec_string(string_a)
        # Snap-taking isn't quite instantaneous :(
        time.sleep(1)
        # Clone the file (cp -c path_to_snapshot_of_file cloned_file)
        newpath = "/ifs/.snapshot/%s"%self.snapname
        newpath = self.srcpath.replace("/ifs",newpath)
        srcfile = "%s/%s"%(newpath,self.filename)
        string_b = "cp -c %s %s"%(srcfile,self.clonefile)
        exec_string(string_b)

    def write(self):
        blocksize = random.randint(1,256)
        count = random.randint(1,256)
        # If I were smart, I'd check the file size and make
        # sure not to seek past the end.
        seek = random.randint(1,256)
        string_g = "qadd -q bs=%dk count=%d of=%s seek=%d oflag=sync conv=notrunc"%(blocksize,count,self.clonefile,seek)
        exec_string(string_g)

def exec_string(e_str):
    if debug: print "exec'ing string:%s"%(e_str)
    output = subprocess.Popen(e_str, shell=True, stdout=subprocess.PIPE)
    # Wait for subprocess to finish:
    response = output.communicate()
    if response:
        if debug: print "Output from execing %s:%s"%(e_str,str(response))
    return(response[0])

def main():
    # 1) Make a file.  
    # 2) Clone it.  
    # 3) Either do a random write to a clone, or make another clone.  
    #    Making another should be rare.

    # Setup
    
    # Make a clones directory
    clonepath="/ifs/data/clones"
    exec_string("mkdir -p %s"%(clonepath))

    # Let's name files uniquely
    uniq = exec_string('date "+%m.%d.%H.%M.%S"').rstrip()

    # But not totally anonymously
    host = exec_string('hostname').rstrip()

    # You have to have snaps licensed
    if not exec_string("isi license | grep SnapshotIQ | grep -o Eval"):
        exec_string("isi_get_license; sleep 10")

    # 1
    # Make the source file; name it whatever's on the commandline or hostname
    try:
        if sys.argv[1]:
            filename = sys.argv[1]
    except:
        filename=host
    srcpath="/ifs/data/source"
    make_file(srcpath,filename)

    # 2
    # Clone the source file
    snapname = "snap_%s"%(uniq)
    c = Clone(host,
              snapname,
              srcpath,
              filename,
              clonepath,
              uniq)
    c.make()

    # 3
    for i in range(1,loop_num):
        # every 1 out of X times, make a clone
        j = random.randint(1,loop_num/1000)
        if j == 1:
            c1 = Clone(host,
                       snapname+str(i),
                       srcpath,
                       filename,
                       clonepath,
                       uniq+str(i))
            c1.make()
        # otherwise, do a random write
        c.write()
        # Let the user know where we're at
        date = exec_string('date').rstrip()
        print "Iter %d, %s:"%(i,date)
 
if __name__ == '__main__':
    main()
