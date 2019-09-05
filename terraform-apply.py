''' This is a python script to run the terraform apply -auto-approve and track the time for the code completion
'''

#!/usr/bin/python
import os
import subprocess
import time
path = "/home/rv965d/nc-rdm57b-terraform/os-nc-terraform"
current = os.getcwd()
print("current directory is %s" % current)
os.chdir(path)

start_time = time.localtime()

print("Timer started at %s" % time.strftime('%X', start_time))

code = subprocess.call(['terraform', 'apply' , '-auto-approve'])
if code == 0:
  print("code executed successfully")
else:
  print("error code is %i" % code)


stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print("Timer stopped at %s" % time.strftime('%X', stop_time))

print("Total time: %s seconds" % difference)
