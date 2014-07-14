#!/usr/bin/python
#-*- coding: utf-8 -*-
from math import log

#文章の読み込み
documents = []
for i in range(50):
    path = '../data/tweet/tweet' + str(i+1) + '.txt'
    f = open(path,'r')
    words = f.readline().rstrip('\n').split(' ')
    documents.append(words)
    f.close()
print "読み込み終了"

#tf idfの計算
result = []
for i in range(50):
    tfidf = {}
    for word in documents[i]:
        if not(tfidf.has_key(word)):
            df = 0
            for j in range(50):
                if word in documents[j]:
                    df += 1
            tfidf[word] = float(documents[i].count(word)) / len(documents[i]) * log(50.0/df)
    result.append(tfidf)
    print '文章%dの計算終了'%(i+1)

#各文章でtfidfが大きいトップ10の単語を表示
for i in range(50):
    print "-------文章%dの特徴語--------"%(i+1)
    tfidf = result[i]
    for k,v in sorted(tfidf.items(), key=lambda x:x[1], reverse=True)[0:10]:
        print k,v
