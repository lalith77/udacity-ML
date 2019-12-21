#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""


from sklearn.svm import SVC
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

print("type of features_train is:", type(features_train))
# taking a sample of data to speed up training time 
# len1 = round(len(features_train)/100)
# len2= round(len(labels_train)/100)
# print("lengths are: ",len1, len2)
# features_train = features_train[0:len1] 
# labels_train = labels_train[0:len2]
clf = SVC(C=10000.0,kernel='rbf')
t0= time()
clf.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")

t0=time()
y=clf.predict(features_test)
print("predicting time:", round(time()-t0, 3), "s")
print(clf.score(features_test, labels_test))
print("The 10th, 26th and 50th element predictions are:", y[10],y[26], y[100])
count=0
for i in y:
    if(i ==1):
        count=count+1
print("Count is: ", count)

#########################################################
