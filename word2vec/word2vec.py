#!/user/bin/python
#-*- coding:utf-8 -*-
import sys
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) # 今どれくらい処理が進んでるか確認する用
sentences = word2vec.Text8Corpus('data/wakati_bocchan.txt')
model = word2vec.Word2Vec(sentences, size=200) 

def s(posi, nega=[], n=5):
    cnt = 1
    result = model.most_similar(positive = posi, negative = nega, topn = n)
    print '順位', '単語', '類似度'
    for r in result:
        print cnt, r[0], r[1]
        cnt += 1

