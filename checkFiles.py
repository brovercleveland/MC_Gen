#!/usr/bin/env python
import sys, os
import subprocess

def checkFiles(selection):
  proc = subprocess.Popen(["bash -c 'wc -l <(ls -1 testOut{0}_pdf7)'".format(selection)],stdout=subprocess.PIPE, shell=True)
  (out,err) = proc.communicate()
  proc2 = subprocess.Popen(["bash -c 'wc -l <(ls -1 res{0}_pdf7)'".format(selection)],stdout=subprocess.PIPE, shell=True)
  (out2,err2) = proc2.communicate()
  num1 = int(out.rsplit(" ")[0])
  num2 = int(out2.rsplit(" ")[0])
  print num1, num2/3
  if num1 == num2/3: print 'ALL JOBS FINISHED'
  else: print "SOME JOBS HAVEN'T FUCKING FINISHED GODDAMNIT!"






if __name__=="__main__":
  if len(sys.argv)==2:
    checkFiles(sys.argv[1])
  else:
    #answer = hadd()
    print "You need 1 argument, asshole"
