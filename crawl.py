import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('http://www.dpxq.com/hldcg/search/view_m_118126.html')
 
# check status code for response received
# success code - 200
# r.encoding = None
html = r.content
print(html.decode('unicode_escape'))
 
# Parsing the HTML
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())