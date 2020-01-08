#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
#from tester import dump_classifier_and_data
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','from_poi_to_this_person'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "rb") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
#print("The keys are : ", data_dict.keys())
#print(data_dict.pop('TOTAL'))
data_dict.pop('TOTAL')
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
print("type of data is:", type(data))
print("shape of data is:", data.shape)

print(len(data[0]))
print(len(data[1]))


labels, features = targetFeatureSplit(data)

print("type of labels:",type(labels))
print("type of features:", type(features))
print(features)
print("length of labels is: {} and length of features is {}: " .format(len(labels) ,len(features)))

for i in range(0,len(features)):
    plt.scatter(i, features[i][0])
    
plt.xlabel("index")
plt.ylabel("salary")
plt.show()
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 42)

clf = tree.DecisionTreeClassifier(min_samples_split=5)
clf.fit(features_train, labels_train)

print("score is:", clf.score(features_test,labels_test))

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# # Provided to give you a starting point. Try a variety of classifiers.
# from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()

# ### Task 5: Tune your classifier to achieve better than .3 precision and recall 
# ### using our testing script. Check the tester.py script in the final project
# ### folder for details on the evaluation method, especially the test_classifier
# ### function. Because of the small size of the dataset, the script uses
# ### stratified shuffle split cross validation. For more info: 
# ### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# # Example starting point. Try investigating other evaluation techniques!
# from sklearn.cross_validation import train_test_split
# features_train, features_test, labels_train, labels_test = \
#     train_test_split(features, labels, test_size=0.3, random_state=42)

# ### Task 6: Dump your classifier, dataset, and features_list so anyone can
# ### check your results. You do not need to change anything below, but make sure
# ### that the version of poi_id.py that you submit can be run on its own and
# ### generates the necessary .pkl files for validating your results.

# dump_classifier_and_data(clf, my_dataset, features_list)