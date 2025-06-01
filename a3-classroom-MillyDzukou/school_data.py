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
from utilities import createData, dictOfSchool, userInput
import SchoolStat

FILE_NAME = "Assignment3Data.csv"
def main():
    print("ENSF 692 School Enrollment Statistics")

    # Test during code
    data = createData(all_years)


    # Print Stage 1 requirements here
    print("Shape of full data array: ", data.shape)
    print("Dimensions of full data array: ", data.ndim)

    dico = dictOfSchool(FILE_NAME)
    print(dico)
    # Prompt for user input
    userinput = userInput(dico)
    print(userinput)

    # TODO: function that will convert user input into number from 1 to 20
    number = 16

    new_school = SchoolStat.SchoolStat(data, number)

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    print("\nSchool name:  {0}, School code: {1}".format(dico.get(userinput), userinput))

    
    # Print the mean enrolment for each grade in school
    for i in range(10,13):
        print("Mean enrolment for grade {0}: {1}".format(i, new_school.meanEnrol(i)))

    print("The Highest enrollment for a single grade: {0}".format(new_school.highestEnrol()))

    print("The lowest enrollment for a single grade: {0}".format(new_school.lowestEnrol()))

    for i in range(2013, 2023):
        print("Total enrollment for {0}: {1}".format(i, new_school.totalEnrol(i)))

    print("Total ten years enrolment: {0}".format(new_school.total10Enrol()))
   
    # TODO: mean enrollment
    print("Mean total enrollment over 10 years: {0}".format(new_school.meanEnrol10()))
    print("For all enrolment over 500, the median value : {0}".format(new_school.medianEnrolOver500()))
    
    

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    print("Mean enrollment in 2013: {0}".format(new_school.meanEnrolYearly(2013)))

    print("Mean enrollment in 2022: {0}".format(new_school.meanEnrolYearly(2022)))

    print("Total graduating class of 2022: {0}".format(new_school.totalGraduate(2022)))

    print("Highest enrollment for a single grade: {0}".format(new_school.higestEnrolGrade()))

    print("Lowest enrollment for a single grade: {0}".format(new_school.lowestEnrolGrade()))


    


if __name__ == '__main__':
    main()

