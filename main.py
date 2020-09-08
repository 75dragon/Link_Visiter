#!/usr/bin/env python
import urllib.request
from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    print("visiting pages")
    f = open("link.txt", "r")
    line = f.readline() #first line is #
    line = f.readline()
    while line:
      line = line.rstrip('\n')
      print("visiting " + line)
      url = urllib.request.urlopen(line)
      print("code: " + str(url.getcode()))
      line = f.readline()
    f.close()

scheduler = BlockingScheduler()
f = open("link.txt", "r")
inter = f.readline().rstrip('\n')
f.close()
if not (inter) or not inter.isnumeric():
    print("forgot time interval on first line, or its not a number")
else:
    scheduler.add_job(some_job, 'interval', minutes=int(inter))
    scheduler.start()
