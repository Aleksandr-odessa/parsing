import requests
import urllib
from bs4 import BeautifulSoup
import csv

FILE_NAME = 'vacancies.csv'

url_parts = ['https', 'www.work.ua', '/jobs-python/', '', '']
url = urllib.parse.urlunsplit(url_parts)

employment = '74+76'
experience = '1'
days='123'
params = {'employment': employment, 'experience': experience,'days':days}

response = requests.get(url, params=params)
soup = BeautifulSoup(response.text, 'lxml')
vacancies_names = soup.find_all(
    'div', class_='card card-hover card-visited wordwrap job-link')
vacancies_info = soup.find_all(
    'p', class_='overflow text-muted add-top-sm cut-bottom')

URL_addres = []
work_name = []
for name in vacancies_names:
    work_name.append(name.a['title'])
    URL_addres.append('https://www.work.ua'+name.a['href'])
work_info = [info.text for info in vacancies_info]

zipped_values = zip(work_name,work_info,URL_addres)
zipped_vacacies =list(zipped_values)

with open(FILE_NAME,'w', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(zipped_vacacies)   
    print('success')