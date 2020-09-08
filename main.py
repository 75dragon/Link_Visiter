#!/usr/bin/env python
import urllib.request

f = open("link.txt", "r")
line = f.readline()
while line:
  line = line.rstrip('\n')
  print("visiting " + line)
  url = urllib.request.urlopen(line)
  print("code: " + str(url.getcode()))
  line = f.readline()
f.close()
