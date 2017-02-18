import subprocess
lookup_user='root'
process_running=0
for line in subprocess.check_output("ps -ef",shell=True).splitlines()[1:]:
    user=line.split()[0]
    if lookup_user == user:
        process_running+=1
print("user %s is running %s processses" %(lookup_user,process_running))

