import requests
from bs4 import BeautifulSoup
import csv
URL = "https://www.educationforever.in/coaching-classes"

r=requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
   
temp=[]       
for link in soup.find_all(class_="event-title"):
    temp.append(link.a.get('href'))

URL="https://www.educationforever.in"
with open("details.csv",'w+') as file:
    writer = csv.writer(file)
    writer.writerow(["NAME","ADDRESS","PHONE NO.","MOBILE NO.","EMAIL","WEBSITE"])
    for link in temp:
        r=requests.get(URL+link)
        soup = BeautifulSoup(r.content, 'html5lib')
        data=str(soup.find(id="ContentPlaceHolder1_lbl_contact_desc")).split("<br/>")
        data.pop(-1)
        while "Pincode -" not in data[0] :
            data.pop(0)
        if "website" in data[-1]:
            data.append(data.pop(0))
        else:
            data[-1]=data[-1]+', '+data.pop(0)
        if data[1].startswith("Fax"):
            data.pop(1)
        name=link[16:].replace('-',' ').capitalize()
        phone=data[0][8:].replace('-',' ').replace('/',',')
        mob=data[1][9:].replace('-',' ').replace('/',',')
        writer.writerow([name,data[-1],phone,mob,data[2][11:],data[3][10:]])
