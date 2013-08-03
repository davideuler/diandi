# -*- coding: utf-8 -*-  
import pymongo

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.diandi

## create a collection
sites = db.sites

site = {"region":"上海,长宁区,长宁区","address":"上海市长宁区-娄山关路445弄10号105室", "tel":"02160641423","contact":"02160641423","mailman":"牛五喜","mailtel":"15221502067"}

siteid = sites.insert(site)

print siteid