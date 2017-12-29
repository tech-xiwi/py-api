#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
if sys.version > '3':
    PY3 = True
else:
    PY3 = False

def readFile(fileName):
    if PY3:
        with open(fileName, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        with open(fileName, 'r') as f:
            return f.read().decode('utf-8')

def writeFile(fileName,content,mode = 'a+w'):
    if PY3:
        with open(fileName, mode, encoding='utf-8') as f:
            f.write(content)
    else:
        with open(fileName, mode) as f:
            f.write(content.decode('utf-8').encode('utf-8'))
