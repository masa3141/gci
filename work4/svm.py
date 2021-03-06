#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_digits

#データの読み込み
data = load_digits()

data_train, data_test, label_train, label_test = train_test_split(data.data,data.target)

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