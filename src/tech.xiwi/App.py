#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xiwi"
from model import user
from utils import json_utils,file_utils

user0 = user.User("xiwi",142323243443,"man") 
user0.printUserInfo()

json_utils.printJson({'nickname':'python','gender':'it'})
json_utils.printJson('{"nickname":"golang","age":"7"}')
json_utils.printJson("{\"nickname\":\"xiwi\"}")

json_utils.printJson(user0)

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123},"children":["Tom","Jim","Cook"]}'

x = json_utils.json2Obj(data)
print (x.name, x.hometown.name, x.hometown.id)

print (len(x.children))
for name in x.children:
    print (name)