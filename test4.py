__author__ = 'think'

# coding=gbk
# coding = utf-8

"""
ÄãºÃ
http://zhidao.baidu.com/question/138854675106454205.html
"""

from __future__ import (print_function, unicode_literals)

text = '2014.11  2016.03  '

currentCharIsSpace = False
count = 0
for c in text:
    if currentCharIsSpace:
        if c.isspace():
            count += 1
        else:
            currentCharIsSpace = False
            print(" %s¸ö¿Õ¸ñ" % (count,))
    else:
        if c.isspace():
            count = 1
            currentCharIsSpace = True
        else:
            print(c, end="")

if currentCharIsSpace:
    currentCharIsSpace = False