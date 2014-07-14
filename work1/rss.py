#!/usr/bin/python
#-*- coding: utf-8 -*-

import urllib2, sys
import xml.etree.ElementTree as etree

try:
    topic = sys.argv[1]
except:
    topic = "domestic"
resp = urllib2.urlopen("http://rss.dailynews.yahoo.co.jp/fc/%s/rss.xml"%topic).read()

output ={}
tree = etree.fromstring(resp)
#参考サイト
#http://hikm.hatenablog.com/entry/20090206/1233950923
#http://ja.pymotw.com/2/xml/etree/ElementTree/parse.html
for d in tree.findall(".//item"):
    print d.find(".//title").text