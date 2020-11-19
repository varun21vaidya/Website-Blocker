import time
from datetime import datetime as dt

host_temp=r"Write_path_of-your_python_file"             #temp created file
host_path=r"C:\Windows\System32\drivers\etc\hosts"      #original path
redirect="127.0.0.1"                                    #Localhost IP
website_list=["www.facebook.com","www.instagram.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("working hrs...")
        with open(host_path,"r+") as file:
            content=file.readlines()
            print(content)
            for website in website_list:     
                if website in content:          #check if website is already present  
                    pass
                else:
                    file.write(redirect+"    "+ website +"\n")
    else:
         with open(host_path,"r+") as file:     #rewrites the host file without bloacked websites for fun hours
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()              
         print("fun hrs....")
    time.sleep(5)
