import time
import webbrowser
from datetime import datetime as dt 
import os
#osname = os.name
#if osname=="Mac"or osname=="Linux" :
hosts_file="/etc/hosts"

#elif osname=="Windows":
#	hosts_file=r"C:\Windows\System32\drivers\etc\hosts"

print("Hello User,Kindly add the webistes you want to block")
print("After you are done with adding all the websites kindly press 1")
website_list=[]
while True:
	website=input("Enter website ")
	if website=="1":
		break
	else:
		website_list.append(website)
   
redirect="127.0.0.1"

start_time=int(input("Enter in 24 hour format the time you start your work"))
end_time=  int(input("Enter in 24 hour format the time you generally end your work"))


while True:

	if dt(dt.now().year,dt.now().month,dt.now().day,start_time)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,end_time):
		with open(hosts_file,'r+') as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")
	else:
		with open(hosts_file,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
	time.sleep(120)




