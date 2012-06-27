#!/usr/bin/env python

"""
re_run_latex.py

script to re-run latex whenever the file changes
"""

import sys, os, time

latex_file = sys.argv[1]

pdf_file = latex_file[:-4] + '.pdf'

command = "pdflatex -interaction=nonstopmode %s"%latex_file

last_run = 0
#for i in range(3):
while True: # keep going forever...
    # check modification times
    latex_time = os.stat(latex_file).st_mtime
    try:
        pdf_time = os.stat(pdf_file).st_mtime
    except OSError: # pdf not there
        pdf_time = 0
    
    #print "latex-time:", latex_time
    #print "pdf-time:  ", pdf_time
    if latex_time >= pdf_time and latex_time > last_run:
        print "file has been updated"
        result = os.system(command)
        if result:
            last_run = latex_time
        print "result is:", result
    else:
        print "no change to source file"
    time.sleep(0.25)
