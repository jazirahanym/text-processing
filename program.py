#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import sys

#Читаем файл
#f = open('out.txt')
#text = f.read()
text = sys.stdin.read()

#rexp = re.compile('Мыш[^,.":?!; ]*')
rexp = re.compile('аст\S*', re.UNICODE)

m = rexp.findall(text)

for x in m:
  print(x)

exit()




