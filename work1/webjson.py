#!/usr/bin/python
#-*- coding: utf-8 -*-

import urllib2, sys, json

try:
    cityid = sys.argv[1]
except:
    cityid = "400040" #久留米市

resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%cityid)
#取得したjsonデータを読み込む
data = json.load(resp)
output = {}

#http://tmlife.net/programming/python/python-json-module.html
#見やすく表示する
#print(json.dumps(data, sort_keys=True, indent=4))

#今日、明日、明後日の天気を取得する
for d in data["forecasts"]:
    output[d["dateLabel"]] = d["telop"]
    #print d["dateLabel"],d["telop"]

for k,v in output.items():
    print k,v


