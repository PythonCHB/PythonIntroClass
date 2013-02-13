#!/usr/bin/env python
# $Id: synciq_error_watcher.py $

import os
import sys
import logging
import time
import optparse
from qa.utils import pseudo_term_cmd

SUCCESS = 0

synciq_core = ["isi_migr_sched" ,
               "isi_migr_sworker" ,
               "isi_migr_pworker" ,
               "isi_migrate"]

__COMMAND = pseudo_term_cmd.PTCommand()

# todo move function calls after this line

parser = optparse.OptionParser()
opts,args = parser.parse_args()

if len(args) == 1:
    # first arguement is required to be log file directory
    log_dir = args[0]
else: 
    parser.error("Invalid argument(s) specified: " + str(args) )
    exit(1)

if  os.path.isdir(log_dir) == False:
    parser.error('path "%s" is not a valid directory' % log_dir) 

exit_code = __COMMAND.exec_cmd("sysctl kern.corefile")

"""
find the core location. 
"""

if exit_code : #if command fails, assume /var/crash
    core_location = "/var/crash"
else:
    core_name = __COMMAND.stdout('raw').split()[1]
    
    core_location = os.path.dirnam(core_name)

#start loop to watch for SyncIQ cores
#todo
#stop after finding a core because there is no need to grab logs twice
#Need to move or rename core
#need to time stamp tail output


#while true; do 'isi_for_array ls /var/crash | grep synciq_core

while True:
    core_found = False
    exit_code = __COMMAND.exec_cmd("isi_for_array 'ls %s%s*core*'" % (core_location, os.sep))
    if exit_code == SUCCESS:
	files = __COMMAND.stndout('all') 
        for file_name in files:
	    for core_name in synciq_core:
		if file_name.find(core_name) >= 0:
                    if core_found == False:
                        dump_siq_status()
                    core_found = True
                    move_core_file(core_location, name, log_dir):  

    time.sleep(5)

def dump_siq_status():
    exit_code = __COMMAND.ext_cmd("isi_for_array 'tail -n 100 /var/log/isi_migrate.log > /var/crash/isi_migr_log.tail.%s'" %time.time())
    if exit_code: 
        print "error tailing isi_migratelog"

    exit.code = __COMMAND.ext_cmd("isi_for_array 'tail -n 100 /var/log/messages > /var/crash/message.tail.%s'" %time.time())
    if exit_code:
        print "error tailing messages"

def move_core_file(dir_path, name, dest_path):
    sep=name.find(':') #need to find the colon to distinguish beginning of file name from node name
    file_name=name[sep + 2:]
    node_number=name[sep -1 : sep]
    node_name=name[0: sep]
    suffix='%f' % time.time()
    #create dest directory todo
    cmd="isi_for_array -n %s 'mv %s %s.%s'" % (node_number, os.path.join(dir_name, file_name), os.path.join(dest_path, node_name, file_name), suffix) 
    exit_code = __COMMAND.exec_cmd(cmd)

    #need to test exit code for success or failure

    if exit_code:
        print "failure moving file" # todo fix up error message
    # need to decide if I need to abort at this point

# node number dir_name/file_name dest_path/node_name/file_name suffix

#wait:noignore:nodes[1]:cont: sysctl kern.corefile
# testmgr synctax

# if core found do:
# grab last 100 lines from /var/log/messages and /var/log/isi_migrate.log
# save them to qalogserver path $$log

# Grab SyncIQ information
# isi sync pol ls -v (find synciq python module to do that?
# isi sync pol report ls -v (find synciq python module to do this)
# gzip /ifs/.ifsvar/modules/tsm to qalogserver

# extra credit
# after core, mount buildbiox and load up symbols
# find version via uname or python equilivant and cd to correct path
# run gdbcore /usr/bin/*executable* <path to core>/core



