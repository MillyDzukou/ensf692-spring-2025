# calgary_dogs.py
# AUTHOR Milly Dzukou
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

def main():

    # Import data here
    # TODO Create a dataframe with data from CalgaryDogBreeds.xlsx
    # TODO Do not modify the files, can change index
    #dog_data =

    print("ENSF 692 Dogs of Calgary")

    # User input stage
    # TODO : prompt dog breed(upper case, lower case, mix case)
    """       check if it's a breed
            no: KeyError “Dog breed not found in the data. Please try again.” and prompt again
            yes continue the program
            end the program after analysis """


    # Data analysis stage
    #one multi-index Pandas DataFrame, at least one IndexSlice object,
    # at least one masking operation, at least one grouping operation,
    # and at least one built-in Pandas or NumPy computational method.

    # TODO: Find and print all years where the selected breed was listed in the top breeds.

    # TODO: Calculate and print the total number of registrations of the selected breed found in the dataset.

    # TODO: Calculate and print the percentage of selected breed registrations out of
    # the total percentage for each year (2021, 2022, 2023).

    # TODO Calculate and print the percentage of selected breed registrations out of the total three-year percentage.

    # TODO Find and print the months that were most popular for the selected breed registrations. Print all months that tie.


if __name__ == '__main__':
    main()
