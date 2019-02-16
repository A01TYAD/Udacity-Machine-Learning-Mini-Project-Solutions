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
    uncleaned_data = []
    

    ### your code goes here
    i = len(ages)
    for a in range(i):
        error = net_worths[a][0]-predictions[a][0]
        uncleaned_data.append((ages[a][0], net_worths[a][0], abs(error)))
    print("number of entries before cleaning", len(uncleaned_data))
    for b in range(9):
        lagrest_error = uncleaned_data[0][2]
        i = len(uncleaned_data)
        for a in range(i):
            if lagrest_error < uncleaned_data[a][2]:
               lagrest_error = uncleaned_data[a][2]
               largest_error_number = a
        print("deleted:",uncleaned_data[largest_error_number])
        del uncleaned_data[largest_error_number]
    cleaned_data = uncleaned_data
    print("number of entries after cleaning", len(uncleaned_data))
    return cleaned_data
    

