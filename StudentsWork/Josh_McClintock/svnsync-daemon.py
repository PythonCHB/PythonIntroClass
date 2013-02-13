#!/usr/bin/python

import daemon
import daemon.pidlockfile
import os
import subprocess
import datetime
import time
import socket
import signal
import sys

CFGFILE = '/etc/svnsync-daemon/svnslaves'
FAILSTRING = "Failed to get lock on destination repos, currently held by 'svn3.west.isilon.com"
#CHILDPIDS = set()



class SvnSyncer(object):
    def __init__(self,hostname):
        self.logpath = ''.join(['/var/log/svnsync-daemon/', hostname, '.log'])
        self.process = None
        self.hostname = hostname
        self.seek = 0

    def startsync(self):
        f = open(self.logpath, 'a')
        self.seek = f.tell()
        
        self.process = subprocess.Popen(['svnsync','sync','https://%s/svnsync' % self.hostname], stdout = f, stderr = subprocess.STDOUT)
        #CHILDPIDS.add(self.process.pid)
        self.writemsg("Starting svnsync for %s with PID %d." % (self.hostname,self.process.pid))

    def checkfail(self):
        if not os.path.exists(self.logpath):
            return False

        f = open(self.logpath, 'r')
        f.seek(self.seek)
        content = f.read()
        self.seek = f.tell() - len(FAILSTRING)
        f.close()
        return FAILSTRING in content

    def isrunning(self):
        if self.process is None:
            return False
        return self.process.poll() is None

    def writemsg(self,msg):
        curdate = datetime.datetime.now()
        curdate = str(curdate) + ': '
        f = open(self.logpath, 'a')
        f.write(str(curdate))
        f.write(msg)
        f.write('\n')
        f.close()

#def killChildrenandSelf(signal):
#    svnSync.writemsg("Detected signal %s" % signal)
#    for pid in CHILDPIDS:
#        os.kill(pid, 15)
#        sleep(2)
#        os.kill(pid, 9)
#    sys.exit(0)

def getSVNSlaves(cfgfile=CFGFILE):
    slaves = []
    f = open(cfgfile)
    for c in f:
        if(c.startswith('#')):
            continue
        slaves.append(c.rstrip('\n'))
    f.close()
    return slaves


def doSyncSlave(svnslaves):
    svnSync.writemsg("Initializing SVN Slaves from %s." % CFGFILE)
    syncers = []
    for slave in svnslaves:
        syncers.append(SvnSyncer(slave))

    while True:
        for syncer in syncers:
            if syncer.checkfail():
                svnSync.writemsg("Detected lock file for %s, removing and restarting..." % syncer.hostname)
                syncer.writemsg("Detected lock file for %s, removing and restarting..." % syncer.hostname)
                subprocess.Popen(['svn', 'propdel', 'svn:sync-lock', '-r0', '--revprop', 'https://%s/svnsync' % syncer.hostname], stdout = open(syncer.logpath, 'a'), stderr = subprocess.STDOUT)

        for syncer in syncers:
            if not syncer.isrunning():
                svnSync.writemsg("Starting svnsync for %s." % syncer.hostname)
                syncer.startsync()
        time.sleep(60)



# Log the fact we started up
svnSync = SvnSyncer(socket.gethostname())
svnSync.writemsg("Master SVN Sync Daemon Starting")

# Daemonize and start doSyncSlave()
D = daemon.DaemonContext(pidfile=daemon.pidlockfile.PIDLockFile('/var/run/svnsync-daemon/svnsync-daemon.pid'),stdout=sys.stdout,stderr=sys.stderr)
with D:
    doSyncSlave(getSVNSlaves())
