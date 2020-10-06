import requests
from bs4 import BeautifulSoup
import pandas

data = []
w = ['https://www.sulekha.com/engineering-colleges/mumbai']
for x in w:
    r = requests.get(x)
    c = r.content

    soup = BeautifulSoup(c, 'html.parser')
    qus = soup.find_all('div', {'class': 'head'})
    for i in qus:
        d = {}
        d['name'] = i.find('h3').text
        print(d)
'''    
d.append(j)
data.append(d)
df = pandas.DataFrame(data)
df.to_csv('op.csv')
'''

