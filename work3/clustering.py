#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
import random

random.seed(1)
data = load_digits().data
label = load_digits().target
nums = []
data_test= []
label_test = []
while len(nums) != 100:
    num = random.randint(0,len(data)-1)
    if not(num in nums):
        nums.append(num)
        data_test.append(data[num])
        label_test.append(label[num])


#データの読み込み
#data_train, data_test, label_train, label_test = train_test_split(data.data,data.target)#label = load_digits().target

print len(data_test)
ids = {}
label_ids = {}
label_ids2 = {}
for i in range(len(data_test)):
    ids[i] = {}
    ids[i][i] = data_test[i]
    label_ids.setdefault(label_test[i],[])
    label_ids[label_test[i]].append(i)
    label_ids2[i] = label_test[i]


print len(data_test)
print np.shape(data_test)
def euclidean(x1,x2):
    return np.sum(np.sqrt(np.power(x1-x2,2)))


for i in range(90):
    print i
    min_d = 999999
    x1,x2 = 0,0
    for k1,v1 in ids.items():
        for k2,v2 in ids.items():
            if k1 != k2:
                d = euclidean(np.average(v1.values(),axis=0), np.average(v2.values(),axis=0))
                if d < min_d:
                    print d,min_d
                    #print "min"
                    x1 = k1
                    x2 = k2
                    min_d = d
    ids[x1].update(ids[x2])
    del ids[x2]
print len(ids)
for k,v in ids.items():
    print "key=%s,key=%s" %(k,v)
print ids
print label
print "予測"
for k,v in ids.items():
    print "-----クラスタ%d---------"%(k)
    for kk,vv in v.items():
        print kk,label_ids2[kk]

print "正解"
for k,v in label_ids.items():
    print '-----ラベル%d-----'%(k)
    for l in v:
        print l
#一番距離が近いもの同士を結合する


