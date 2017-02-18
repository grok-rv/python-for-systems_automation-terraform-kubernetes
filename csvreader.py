import csv
try:
    filename='/Uers/rreddy/pythontut/servers.csv'
    with open(filename) as file_handle:
        reader=csv.reader(file_handle)
        os_counts={}
        for row in reader:
            os_counts[row[2]]=os_counts.get(row[2],0)+1
        print(os_counts)
except Exception as ex:
    print("A %s exception has occured because of %s" %(type(ex).__name__,ex.args))
else:
    print("all goood")

