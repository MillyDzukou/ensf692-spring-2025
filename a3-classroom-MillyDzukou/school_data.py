# school_data.py
# Milly DZUKOU
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.
import csv

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here
all_years = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

# You may add your own additional classes, functions, variables, etc.
from utilities import create_data, dict_of_school, verify_user_input, school_line
import SchoolStat

FILE_NAME = "Assignment3Data.csv"
def main():
    print("ENSF 692 School Enrollment Statistics")

    # Create our data structure
    data = create_data(all_years)

    # Create a dictionary with the school code and school name.
    dico = dict_of_school(FILE_NAME)

    # Print Stage 1 requirements here
    print("Shape of full data array: ", data.shape)
    print("Dimension of full data array: ", data.ndim)


     # Prompt for user input
    user_input = verify_user_input(dico) 

    # Convert user input into number from 1 to 20
    school_index = school_line(dico, user_input)

    # Instantiate a new SchoolStat class from the SchoolStat file
    new_school = SchoolStat.SchoolStat(data, school_index)

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    # print the chosen school and corresponding code.
    print("School name:  {0}, School code: {1}".format(dico.get(user_input), user_input))

    # Print the mean enrolment for each grade in school
    for i in range(10,13):
        print("Mean enrolment for grade {0}: {1}".format(i, new_school.mean_enrol(i)))

    # Display the highest enrollment for a single grade
    print("The Highest enrollment for a single grade: {0}".format(new_school.highest_enrol()))

    # Display a single enrollment for a single grade.
    print("The lowest enrollment for a single grade: {0}".format(new_school.lowest_enrol()))

    # Display the total enrolment for each year during the 10 years.
    for i in range(2013, 2023):
        print("Total enrollment for {0}: {1}".format(i, new_school.total_enrol(i)))

    # Display the total enrollment for all the ten years.
    print("Total ten years enrolment: {0}".format(new_school.total_ten_enrol()))
   
    # Display the mean total enrollment over the ten years.
    print("Mean total enrollment over 10 years: {0}".format(new_school.mean_enrol_ten()))

    # Display the median value for all the enrollment greater than 500.
    print("For all enrolment over 500, the median value : {0}".format(new_school.median_enrol_over_500()))
    
    

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    print("Mean enrollment in 2013: {0}".format(new_school.mean_enrol_yearly(2013)))

    print("Mean enrollment in 2022: {0}".format(new_school.mean_enrol_yearly(2022)))

    print("Total graduating class of 2022: {0}".format(new_school.total_graduate(2022)))

    print("Highest enrollment for a single grade: {0}".format(new_school.highest_enrol_grade()))

    print("Lowest enrollment for a single grade: {0}".format(new_school.lowest_enrol_grade()))

    


    


if __name__ == '__main__':
    main()

