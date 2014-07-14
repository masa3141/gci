#!/usr/bin/python
#-*- coding: utf-8 -*-

import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_digits
from sklearn.grid_search import GridSearchCV

#データの読み込み
data = load_digits()

data_train, data_test, label_train, label_test = train_test_split(data.data,data.target)

#学習する
print '学習開始'
parameters = {'kernel':('linear', 'poly', 'rbf', 'sigmoid'), 'C':[0.1,1,10,100]}
estimator = SVC()
clf = GridSearchCV(estimator, parameters)
clf.fit(data_train, label_train)
print clf.grid_scores_
