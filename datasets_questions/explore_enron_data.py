
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

enron_data = pickle.load(
    open("../final_project/final_project_dataset.pkl", "rb"))


print("length of dictionary is : ", len(enron_data))
print("The keys are : ", enron_data.keys())
print("The number of features for each person are :",
      len(enron_data["BAXTER JOHN C"].keys()))
print("The features are:", enron_data["BAXTER JOHN C"].keys())

people = enron_data.keys()
poi_count = 0
for i in people:
    if (enron_data[i]["poi"] == 1):
        poi_count = poi_count+1

print("The number of persons of interest are :", poi_count)

print("The total stock value for James Prentice is:",
      enron_data["PRENTICE JAMES"]["total_stock_value"])

print("Number of emails from Colwell wesley to poi",
      enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print("Value of exercised stock options by Jeffrey Skilling",
      enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

people_without_payments = 0
for i in people:
    if (enron_data[i]['total_payments'] == 'NaN'):
        people_without_payments = people_without_payments+1
print("Percentage of people without payments is",
      (people_without_payments / len(people)) * 100)
