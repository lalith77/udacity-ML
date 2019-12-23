#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    # your code goes here
    errors = []

    for i in range(0, len(predictions)):
        errors.append(abs(net_worths[i] - predictions[i]))

    # runs a loop 10 times and deletes the values with the max error .
    # so top 10 errors are  removed
    # converting numpy arrays to lists to use the pop method
    ages = ages.tolist()
    net_worths = net_worths.tolist()
    for i in range(0, 9):
        index = errors.index(max(errors))
        errors.pop(index)
        ages.pop(index)
        net_worths.pop(index)

    print("length of lists after removing outliers is:", len(errors))

    # zip returns a list of tuples in python 2
    # in python 3, it returns a zip object, convert it to a list using list() func
    cleaned_data = list(zip(ages, net_worths, errors))
    return cleaned_data
