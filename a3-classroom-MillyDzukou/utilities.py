# This file contains all the functions that are necessary
# to realize our program but cannot be bind for logical reason with other parts
# of the program directly.
import numpy as np
import csv

def create_data(lst_year):
    """ 
    create_data function takes a list of years (years are ndarrays)
    and return a ndarray of (10,20,3) which contains all
    data.
    dim 0 is the year
    dim 1 is the school
    dim 2 is the grade (10,11,12)

    Attributes:
        lst_year (list(ndarray)): contain the list of all the data by per year.
    """
    # Create the shape of the return data.
    data = np.ndarray(shape = (10,20,3))

    # Loop over the list by index
    # assign the reshape data (target size: (20,3) to the corresponding index 
    for i in range(len(lst_year)):
        data[i] = np.reshape(lst_year[i], newshape=(20,3))

    return data

def verify_user_input(dico):
    """
    verify_user_input ask a school name or code, checks if it corresponds to one of the school
    and return the school code of this school if it exists.
    Attributes:
        dico(school code: school name): contains the values code and school

    return:
        string: school code
    """
    user_input = input("Please enter the high school name or school code: ")
    
    # checks if the user input corresponds to keys or values
    if user_input not in dico.keys():
        if user_input not in dico.values():
            raise ValueError("Enter a valid school name or school code")
        else:
            # loop over the items in dictionary
            # Checks if it correspond the input correspond to a school name
            # insert in a list
            # and the take the first elemet of the list 
            user_input = [item[0] for item in dico.items() if item[1]==user_input][0]

    return  user_input


def dict_of_school(filecsv):
    """
    dict_of_school function takes a csv file format 
    and determine the all the school name and relevant school code.

    Attributes:
        filecsv (str): name of the file in csv format.

    return:
        dico(str:str): dictionary of school code and school name.
    """
    # Open the file 
    # Read it
    # Initialize a list for code
    # Initialize an empty dictionary
    # Loop over the row inside the reader and
    # extract index 1(school code) and 2(school name)
    # check if the code is already in the list code
    # if not add the code to the list code
    # and add the pair to our dictionary
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
    
    # Sort the dictionnary to have the smallest school code first
    dico = dict(sorted(dico.items()))

    return dico


def school_line(dico, code):
    """
    school_line function determines if a given code is present in school
    code and determine at which index you can find it in a sorted array.

    Attributes:
        dico(dictionary): contains the school code and school name.
        code(str): given school code

    return
        int: index of the school code
    """
    lst_school_code = list(dico.keys())
    for i in range(len(lst_school_code)):
        if lst_school_code[i] == str(code):
            return i
    return "Unable to find the index of this school"