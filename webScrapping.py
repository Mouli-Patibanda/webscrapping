import requests
from bs4 import BeautifulSoup
r = requests.get('https://stackoverflow.com/questions/tagged/python')
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', id= 'questions')
# print(s)
lines=s.find_all('a',class_='s-link')
for line in lines:
    print(line.text)


 

