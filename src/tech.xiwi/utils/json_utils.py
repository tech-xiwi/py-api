#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from collections import namedtuple
from datetime import datetime
import sys
if sys.version > '3':
    PY3 = True
else:
    PY3 = False

# 用户自定义类    
def obj2dict(obj):
    dd = {}
    # 展开它的属性
    for m in dir(obj):
        if m[0] != "_" :
            value = getattr(obj, m)
            if not callable(value):
                dd[m] = obj2Json(value)
    return dd
    
def list2json(data):
    res_list = []
    for item in data:
        value = obj2Json(item)      
        res_list.append(value)  
    return res_list 
    
def dict2json(data):
    res = {}
    for item in data:
        res[item] = obj2Json(data[item])
    return res
    
# complex obj to json
# 复杂对象转换json对象 (dict、list)
def obj2Json(obj):
    # list, set, tuple
    if isinstance(obj,(list, set, tuple)):
        return list2json(obj)
    # dict
    elif isinstance(obj,dict):
        return dict2json(obj)
    # 基本类型 py3里面只有int没有long, py3里只有str 没有 basestring
    # int, long, basestring, bool, float
    elif obj == None or isinstance(obj, (int, int if PY3 else long, str if PY3 else basestring, bool, float)):
        return obj
    elif isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    # 用户自定义的类
    else:
        return obj2dict(obj)

def printJson(data):
    print (formatJson(data))

def formatJson(data):
    if isinstance(data,str):
        data = json.loads(data)
    try:
        json_data_str = json.dumps(data, sort_keys=True, indent=4, separators=(',',':'))
    except Exception as e:
        json_data_str = formatJson(obj2Json(data))
    return json_data_str

# Parse JSON into an object with attributes corresponding to dict keys.
def json2Obj(data):
    return json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))