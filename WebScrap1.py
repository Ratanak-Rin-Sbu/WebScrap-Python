from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.arirang.com/News/News_list.asp?sys_lang=Eng&category=0').text
soup = BeautifulSoup(html_text, 'lxml')

section = soup.find('ul', class_='aNews_list')
news = section.find_all('h4')
links = section.find_all('a', href=True)
n = len(news)
for i in range(1, n):
    print(i, end=". ")
    print(news[i].text)
    print('http://www.arirang.co.kr/News/' + links[i]['href'])
    print()