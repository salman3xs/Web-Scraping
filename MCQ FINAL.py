import requests
from bs4 import BeautifulSoup
import pandas

sites=['https://www.gkseries.com/general-knowledge/geography/geo-tectonics/geography-mcqs',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/00002-geo-tectonics',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/3-geo-tectonics-objective-questions-and-answers',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/4-geo-tectonics-quiz-questions-and-answers',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/5-geo-tectonics-questions-and-answers-on-earth',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/6-geo-tectonics-interview-questions-and-answer',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/7-geo-tectonics-objective-questions-and-answers',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/8-geo-tectonics-objective-questions-and-answers',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/9-geo-tectonics-quiz-questions-and-answers',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/10-geo-tectonics-interview-questions-and-answer',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/11-geo-tectonics-interview-questions-and-answer',
        'https://www.gkseries.com/general-knowledge/geography/geo-tectonics/12-geo-tectonics-objective-questions-and-answers']
data = []
for x in sites:
    r = requests.get(x)
    c = r.content

    soup = BeautifulSoup(c, 'html.parser')
    qus = soup.find_all('div', {'class': 'mcq'})
    for i in qus:
        d={}
        d['Question'] = i.find('div', {'class': 'question-content clearfix'}).text.replace('\n', '').replace('\t', '').replace('\r', '')
        op = (i.find_all('div', {'class': 'col-md-12 option'}))
        d['op1'] = op[0].text.replace('\n', '').replace('\t', '').replace('\r', '').replace('A', '')
        d['op2'] = op[1].text.replace('\n', '').replace('\t', '').replace('\r', '').replace('B', '')
        d['op3'] = op[2].text.replace('\n', '').replace('\t', '').replace('\r', '').replace('C', '')
        d['op4'] = op[3].text.replace('\n', '').replace('\t', '').replace('\r', '').replace('D', '')
        data.append(d)
df = pandas.DataFrame(data)
df.to_csv('output.csv')
