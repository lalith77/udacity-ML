#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from sklearn.preprocessing import MinMaxScaler
#from tester import dump_classifier_and_data
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','total_payments','total_stock_value','from_poi_to_this_person'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "rb") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
#print("The keys are : ", data_dict.keys())
#print(data_dict.pop('TOTAL'))
data_dict.pop('TOTAL')

for name in data_dict:
    for feature in ['total_stock_value','total_payments']:
        if data_dict[name][feature] == 'NaN':
            data_dict[name][feature] = 0
for name in data_dict:
    stock = float(data_dict[name]['total_stock_value'])
    total_value = float(data_dict[name]['total_payments'] )+ stock
    data_dict[name]['total_money'] = total_value
    print("total money for {} is {}".format(name, total_value))
features_list = ['poi','total_money','from_poi_to_this_person'] 

dict_len = data_dict.keys()
print(dict_len)
for i in range(0,dict_len):
    plt.scatter(i, data_dict[i]['from_poi_to_this_person'])
    
plt.xlabel("index")
plt.ylabel("emails")
plt.show()

my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
print("type of data is:", type(data))
print("shape of data is:", data.shape)

print(len(data[0]))
print(len(data[1]))
print("data[0] before scaling is:",data[0])
scaler = MinMaxScaler()
print(scaler.fit(data))

print("Max data is:",scaler.data_max_)
data =scaler.transform(data)
print("data[0] after transform",data[0])

labels, features = targetFeatureSplit(data)

print("type of labels:",type(labels))
print("type of features:", type(features))
# print(features)
print("length of labels is: {} and length of features is {}: " .format(len(labels) ,len(features)))


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