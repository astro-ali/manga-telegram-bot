# Project Path ---> Desktop\manga bot
from bs4 import BeautifulSoup
import requests
import re

page_src = requests.get("https://manga.ae/1shinge-kino-kyojin/").text
soup = BeautifulSoup(page_src, 'lxml')
last_tag = soup.find_all('a', class_='chapter')[0].text
chapter_number = re.findall(R'\d\d\d\d|\d\d\d|\d\d|\d',last_tag)

last_chapter = int(chapter_number[0])

print(f"Available chapters:[1-{last_chapter}]")
