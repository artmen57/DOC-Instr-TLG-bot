import sys 

from time import sleep
import os
from psutil import disk_usage
from psutil._common import bytes2human
def clear():
    os.system( 'cls' )

a = disk_usage("C:\\")
a = bytes2human(a.used)
b = 5
c =10

while c<20: 
  sys.stdout.write("\r" "This is Run : " + str(a) + "\n")
  sys.stdout.write("\r" "This is a : " + str(a) +  "\nThis is b :" +  str(b) + "\nThis is C:"  +str(c) + "\n" )
  
  sleep(0.5)
  b+=1
  c+=1
  sys.stdout.flush()
  clear()