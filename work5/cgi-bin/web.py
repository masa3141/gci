#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2, sys, json
import cgi

print "Content-type: text/html\n"

form = cgi.FieldStorage()
cityid = form.getvalue('area','400040')
#cityid = "400040"
#取得したデータを読み込む
resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%cityid)
data = json.load(resp)
output = {}

#今日、明日、明後日の天気を取得する
for d in data["forecasts"]:
    output[d["dateLabel"]] = d["telop"]
res = ''
for k,v in output.items():
    res += k + u'の天気は' + v + u'です。<br>'
print """
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>CGIスクリプト</title>
</head>
<body>
%s
</body></html>
"""%(res.encode('utf_8') )