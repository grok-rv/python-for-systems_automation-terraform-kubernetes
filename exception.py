#this is an exception
try:
    import module
except Exception as ex:
    print("A %s exception occured running %s" %(type(ex).__name__,ex.args))
else:
    print("all good")

