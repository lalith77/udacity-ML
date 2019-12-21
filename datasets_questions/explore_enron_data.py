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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))


print("length of dictionary is : ", len(enron_data))
print("The keys are : ", enron_data.keys())
print("The number of features for each person are :", len(enron_data["BAXTER JOHN C"].keys()))
print("The features are:", enron_data["BAXTER JOHN C"].keys())

people = enron_data.keys()
poi_count = 0
for i in people:
    if (enron_data[i]["poi"] == 1):
        poi_count= poi_count+1

print("The number of persons of interest are :", poi_count)

print("The total stock value for James Prentice is:",enron_data["PRENTICE JAMES"]["total_stock_value"])

print("Number of emails from Colwell wesley to poi",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print("Value of exercised stock options by Jeffrey Skilling",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
salaried_people= 0
known_email_people = 0
biggest_total_payment= 0
guy_who_took_the_most_money =''
people_with_payments=0
pois_without_payment=0
for i in people:
    if(type(enron_data[i]['total_payments']) == type(5) and i!= 'TOTAL'):
        people_with_payments = people_with_payments+1
        if (enron_data[i]['total_payments'] > biggest_total_payment):
            biggest_total_payment = enron_data[i]['total_payments']
            guy_who_took_the_most_money = i
    if(type(enron_data[i]['salary']) == type(4)):
        salaried_people= salaried_people+1
    if("@" in enron_data[i]['email_address']):
        known_email_people = known_email_people+1
    if(enron_data[i]['total_payments'] == 'NaN' and enron_data[i]['poi']==1):
        pois_without_payment = pois_without_payment+1

print("Guy who took the most money is:",guy_who_took_the_most_money)
print("He took a total of:", biggest_total_payment)
# print(type(enron_data["SKILLING JEFFREY K"]['total_payments']))
# print(type(biggest_total_payment))

print("the salaried people are:", salaried_people)
print("people with emails are:", known_email_people)
print("people with payments are:", people_with_payments)
print("number of pois are:",poi_count)
print("pois without payment are:", pois_without_payment)
print("percentage of pois without payment are:", (pois_without_payment/ poi_count) * 100)
