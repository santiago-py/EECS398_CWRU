# How to get the lyrics from azlyrics.com
from bs4 import BeautifulSoup
import urllib.request
import requests
source = requests.get('https://www.azlyrics.com/lyrics/vampireweekend/harmonyhall.html').text
soup = BeautifulSoup(source, 'lxml')
lyrics = soup.find("div", {"class": "col-xs-12 col-lg-8 text-center"}).find_all("div")[6].get_text()
lines = lyrics.splitlines()[2:]
processed_lyrics = "\n".join(lines)
print(processed_lyrics)
