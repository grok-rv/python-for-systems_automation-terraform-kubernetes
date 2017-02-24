#process disk 
import subprocess
partition_usage_threshold=5
df_cmd=subprocess.check_output(['df','-k'])
#print(df_cmd)
lines = df_cmd.splitlines()
#print lines
for line in lines[1:]:
    columns = line.split()
    used_percentage=columns[4]
    used_percentage=used_percentage.replace('%','')
    #print(used_percentage)
    if int(used_percentage) >= partition_usage_threshold:
        print("partition %s usage is beyond threshold at %s" %(columns[0],columns[4]))

