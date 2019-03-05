# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 00:02:23 2019

@author: msi-1
"""

import requests
param = {"search_query": "還願 音樂"}  # 輸入搜尋的條件
r = requests.get('https://www.youtube.com/results', params=param)
print(r.url)
#webbrowser.open(r.url)

from bs4 import BeautifulSoup
from urllib.request import urlopen
from pytube import YouTube
import os
import time

tStart = time.time()#計時開始
video = [];

html = urlopen(r.url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
#print(html)
course_links = soup.find_all('h3', {"class": "yt-lockup-title"})
#print(course_links)

#for link in course_links:
#    title = link.find_all('a', {"title": re.compile(".*?")})
#    print(title[0]["title"])

#抓幾部影片 ex.3部
for i in range(3):
    title = course_links[i].find('a')
    print(title["title"])
    video.append("https://www.youtube.com"+title["href"])
    try:
        yt = YouTube("https://www.youtube.com"+title["href"])
        location = os.getcwd()
        location = location+'/'
        #stream = yt.streams.filter(only_audio=True).first()
        stream = yt.streams.first()
        stream.download(location)
    except:
        pass
    continue

print('Done!')
tEnd = time.time()#計時結束
print("It cost %f sec" % (tEnd - tStart))#自動進位