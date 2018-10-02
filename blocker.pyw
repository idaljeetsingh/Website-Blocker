'''
    Title		: Website Blocker         
    Author		: Daljeet Singh Chhabra
    Language		: Python
    Date Created	: 03-10-2018
    Last Modified	: 03-10-2018
'''
import time
from datetime import datetime as dt

hosts_path_windows="C:\Windows\System32\drivers\etc\hosts"
hosts_path_linux="/etc/hosts"
redirect="127.0.0.1"

website_list=["www.facebook.com","facebook.com","www.google.com","google.com", "fb.com", "touch.facebook.com", "proxysite.com"]	#Modify the list to block the websites.

work_start=8
work_end=16

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,work_start) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,work_end):	#"Working hours..."
        with open(hosts_path_windows,'r+') as file:																		#Change the hosts_path depending on the OS
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:																												#"Fun hours..."
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    
    time.sleep(60)
