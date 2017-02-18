import subprocess
def fucntionprocessrunning(lookup_user):
    process_running=0
    for line in subprocess.check_output("ps -ef",shell=True).splitlines()[1:]:
        user=line.split()[0]
        if lookup_user==user:
            process_running+=1
    return "user %s has running %s processes" %(lookup_user,process_running)
