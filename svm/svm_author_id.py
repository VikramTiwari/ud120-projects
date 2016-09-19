#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf = SVC(C=10000, kernel="rbf")

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s" # 4.065s

t1 = time()
predictions = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s" # 4.31s

print clf.score(features_test, labels_test)

print "10 >", predictions[10]
print "26 >", predictions[26]
print "50 >", predictions[50]

count = 0;
for i in predictions:
    if i==1:
        count = count + 1

print count
#########################################################
