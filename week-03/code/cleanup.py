# cleanup.py

import os

cPth = r"C:\aaa"
cLog = r"C:\log.txt"

def cleanOver(big):
    for r, d, f in os.walk(cPth, False):
        for name in f:
            ful = os.path.join(r, name)
            siz = os.path.getsize(ful)
            if siz >= big:
                try:
                    hLog.write("Try removing %s\n"%ful)
                    os.remove(ful)
                except Exception as e:
                    hLog.write("%s\n"%e)
        for name in d:
            ful = os.path.join(r, name)
            try:
                hLog.write("Try removing %s\n"%ful)
                os.rmdir(ful)
            except Exception as e:
                hLog.write("%s %s\n"%(type(e),e))

def myPri(header):
    print(header)
    for r, d, f in os.walk(cPth, False): print(r, d, f)

hLog = open(cLog, "w")
myPri("Before")
cleanOver(2)
myPri("After" )
hLog.close()
raw_input("Done")
