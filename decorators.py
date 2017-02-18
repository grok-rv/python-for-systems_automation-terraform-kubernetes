import time
import urllib2
def elapsed_time(function_to_time):
    def wrapper():
        t0=time.time()
        webpage=download_webpage()
        t1=time.time()
        print("the time elapsed for download is %s \n" %(t1-t0))
    return wrapper
def download_page():
    url=""
    response=urllib2.urlopen(url, timeout=60)
    return response.read()

@elapsed_time
webpage=download_page()
