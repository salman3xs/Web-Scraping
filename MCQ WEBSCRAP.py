import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get('https://www.gkseries.com/general-knowledge/geography/geo-tectonics/12-geo-tectonics-objective-questions-and-answers')
c = r.content

soup = BeautifulSoup(c, 'html.parser')
qus = soup.find_all('div', {'class': 'mcq'})
data = []
for i in qus:
    d = {}
    d['Question'] = i.find('div', {'class': 'question-content clearfix'}).text.replace('\n', '').replace('\t', '').replace('\r', '')
    op = (i.find_all('div', {'class': 'col-md-12 option'}))
    d['op1'] = op[0].text.replace('\n', '').replace('\t', '').replace('\r', '')
    d['op2'] = op[1].text.replace('\n', '').replace('\t', '').replace('\r', '')
    d['op3'] = op[2].text.replace('\n', '').replace('\t', '').replace('\r', '')
    d['op4'] = op[3].text.replace('\n', '').replace('\t', '').replace('\r', '')
    data.append(d)
df = pandas.DataFrame(data)
print(df)
