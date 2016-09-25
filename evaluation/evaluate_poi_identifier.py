#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
from sklearn import metrics
import numpy

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)

predictions = clf.predict(features_test)
unique, counts = numpy.unique(predictions, return_counts=True)
all_counts = dict(zip(unique, counts))
print all_counts
total = all_counts[0.0] + all_counts[1.0]

print "POIs:", all_counts[1.0]
print "Total:", all_counts[0.0] + all_counts[1.0]

print "Accuracy for predict=0:", (total - all_counts[1.0]) / float(total)

print metrics.precision_score(labels_test, clf.predict(features_test), average='binary')
print metrics.recall_score(labels_test, clf.predict(features_test), average='binary')


[0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

true_positive = 6
true_negative = 9
false_positive = 3
false_negative = 2

precision = true_positive / float (true_positive + false_positive)
print "Precision:", precision
recall = true_positive / float(true_positive + false_negative)
print "Recall", recall
