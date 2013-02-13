'''
This program will read through my file of useful tips and tricks.
It generates a file that's a table of contents.
Once you've got the table of contents, you can request one
of them, and it'll print out that tip.

At the moment, all it does is build the toc; doesn't print out
the tip yet.
'''

tocfile='tipfile_toc.txt'
tipfile='tipfile.txt'

def cat_file(file,debug):
    if debug: print 'in cat_file; going to cat %s'%file
    f = open(file,'r')
    while True:
        line = f.readline()
        if not line:
            break
        print line,


def toc_gen(debug):
    f = open(tipfile,'r')
    g = open(tocfile,'w')
    entry_num = 1
    while True:
        line = f.readline()
        if not line:
            break
        if '*****' in line: # this will be a header start

            if debug: print 'header start'

            toc_entry = f.readline()

            if debug: print toc_entry[2:],

            g.write('%d: %s'%(entry_num,toc_entry[2:]))
            f.readline() # this will be the end of the header

            if debug: print 'header end'

            entry_num = entry_num + 1
        # the rest of the loop will read in the content
    f.close()
    g.close()
    if debug:
        print "This is what's in %s: \n"%tocfile
        cat_file(tocfile,debug)
