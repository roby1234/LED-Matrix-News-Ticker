#!/usr/bin/python
import feedparser
import time
from subprocess import check_output
import sys

feed_name = 'Zeenews'
url =  'http://zeenews.india.com/rss/india-national-news.xml'

db = '/home/onkar/Desktop/openpixelcontrol-master/python_clients/mywork/news.txt'
limit = 12 * 3600 * 1000

current_time_millis = lambda: int(round(time.time() * 1000))
current_timestamp = current_time_millis()

feed = feedparser.parse(url)


posts_to_print = []
posts_to_skip = []

for post in feed.entries:
    title = post.title
    posts_to_print.append(title)
    
f = open(db, 'w')
for title in posts_to_print:
        #f.write(time.strftime("%a, %b %d %I:%M %p") + "\n")
         f.write(title) 
         f.write('\n')
f.close

with open('news.txt') as f:
  for a in f:
    print(a)


