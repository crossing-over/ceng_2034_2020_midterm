#!/usr/bin/python3 
import os,threading,sys,requests
#1
print("PID is :",os.getpid())


#2

platform = sys.platform
if(platform == "linux"):
	print("Load avgerage is :",os.getloadavg())
	
load_avg = os.getloadavg()
print("The cpu count is : ",os.cpu_count())

#3
load_5_min = load_avg[1]
nproc= os.cpu_count()

if (nproc-load_5_min < 1):
	print("exit...")
	#sys.exit()

#4
array = ["https://api.github.com","http://bilgisayar.mu.edu.tr/","https://www.python.org/","http://akrepnalan.com/ceng2034","https://github.com/caesarsalad/wow"]

def try_req(url):
	
	res = requests.get(url)
	code = res.status_code
	
	
	if 199 < code < 300:
    		print("The url is valid :   "+ url) 
	
	else:
    		print("The url is invalid  :  " + url)
    		
for i in range(0,5):
		
	thread1 = threading.Thread(target=try_req, args=(array[i],))
	thread1.start()
	thread1.join()
	
	

print("End of the script..")


