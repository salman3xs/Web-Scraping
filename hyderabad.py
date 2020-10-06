import requests
from bs4 import BeautifulSoup
import pandas

data = []
w = ['https://www.sulekha.com/engineering-colleges/hyderabad', 'https://www.sulekha.com/mbbs-colleges/hyderabad', 'https://www.sulekha.com/hotel-management-degree-courses/hyderabad', 'https://www.sulekha.com/mba-colleges/hyderabad', 'https://www.sulekha.com/pharmacy-colleges/hyderabad', 'https://www.sulekha.com/nursing-colleges/hyderabad','https://www.sulekha.com/aviation-colleges/hyderabad']
for x in w:
    r = requests.get(x)
    c = r.content

    soup = BeautifulSoup(c, 'html.parser')
    qus = soup.find_all('div', {'class': 'head'})
    for i in qus:
        d = {}
        if i.find('h3')!=None:
            d['Name'] = i.find('h3').text
        if i.find('span', {'class': 'location'})!=None:
            d['Location'] = i.find('span', {'class': 'location'}).text
        if i.find('em')!=None:
            d['Courses'] = i.find('em').text
        if i.find('b', {'class': "icon-phone f-icon isbvn"})!=None:
            d['Contact No.'] = i.find('b', {'class': "icon-phone f-icon isbvn"}).text
        data.append(d)
df = pandas.DataFrame(data)
df.to_csv('hyderabad.csv')
