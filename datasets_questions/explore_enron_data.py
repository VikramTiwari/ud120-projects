#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "people ",len(enron_data)
print "features ",len(enron_data["METTS MARK"])

count = 0
for key, val in enron_data.iteritems():
    if enron_data[key]["poi"]:
        # print key
        count = count + 1
print "POI ", count


count = 0
with open("../final_project/poi_names.txt") as poi_names:
    lines = filter(None, (line.rstrip() for line in poi_names))
    for poi_name in lines:
        count = count + 1
print "POIT ", count-1

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "total payments"
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

count = 0
for key, val in enron_data.iteritems():
    if enron_data[key]["salary"] != 'NaN':
        count = count + 1
print "quantified salary", count

count = 0
for key, val in enron_data.iteritems():
    if enron_data[key]["email_address"] != 'NaN':
        count = count + 1
print "email_address ", count

count = 0
total = 0
for key, val in enron_data.iteritems():
    total = total + 1
    if enron_data[key]["total_payments"] == 'NaN':
        count = count + 1
print "total_payments ", count, total, count*100/total

count = 0
total = 0
for key, val in enron_data.iteritems():
    total = total + 1
    if enron_data[key]["total_payments"] == 'NaN' and enron_data[key]["poi"]:
        count = count + 1
print "total_payments ", count, total, count*100/total
