#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_digits

#データの読み込み
data = np.genfromtxt('../data/kaggle/train.csv',delimiter=",",dtype = np.float,comments="label")
print np.shape(data)
print np.shape(data[:,1:])
print np.shape(data[:,0])
data_train, data_test, label_train, label_test = train_test_split(data[:,1:],data[:,0])

#学習する
print '学習開始'
estimator = LinearSVC(C=1.0)
estimator.fit(data_train, label_train)
#予測する
print '予測開始'
label_predict = estimator.predict(data_test)
#評価する
print confusion_matrix(label_test,label_predict)
print accuracy_score(label_test,label_predict)