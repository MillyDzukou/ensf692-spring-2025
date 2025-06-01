# This file contains all the functions that are necessary
# to realize our program but cannot be bind with other parts
# of the program directly.
import numpy as np
import csv

def createData(lst_year):
    """ This function takes a list of years (years are ndarrays)
        and return a ndarray of (10,20,3) which contains all
        data.
        dim 0 is the year
        dim 1 is the school
        dim 2 is the grade (11,12,13)
    """
    data = np.ndarray(shape = (10,20,3))
    for i in range(len(lst_year)):
        data[i] = np.reshape(lst_year[i], newshape=(20,3))
    return data

def userInput(dico):
    user_input = input("Please enter the high school name or school code: ")
    if user_input not in dico.keys():
        if user_input not in dico.values():
            raise ValueError("Enter a valid school name or school code")
        else:
            user_input = [item[0] for item in dico.items() if item[1]==user_input][0]

    return  user_input


def dictOfSchool(filecsv):
    with open(filecsv, mode='r')as infile:
        reader = csv.reader(infile)
        next(reader) #skip the first row
        codelist= []
        dico = {}
        for rows in reader:
            k = rows[2]
            v = rows[1]
            if k not in codelist:
                codelist.append(k)
                dico[k]=v

    dico = dict(sorted(dico.items()))

    return dico


# def schoolCode():
#     print():
#     user_input = input
#     schoolcode =9000

#     return schoolcode