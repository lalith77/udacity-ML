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
from sklearn.model_selection import train_test_split
from sklearn import tree
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)

clf = tree.DecisionTreeClassifier()
print("Training data ...")
print("The number of features are", len(features_train))
print(features[0])

clf.fit(features_train, labels_train)

my_predictions = clf.predict(features_test)
print("the predictions are:",my_predictions)
print("test labels are:",labels_test)
print("total number of people are:", len(labels))
total_pois= 0
for i in labels:
    total_pois +=i

print("total number of pois are:", total_pois)
print(clf.score(features_test, labels_test))


