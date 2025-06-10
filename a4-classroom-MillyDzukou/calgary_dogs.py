# calgary_dogs.py
# AUTHOR Milly Dzukou
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.
import numpy as np
import pandas as pd


def main():

    # Import data here
    # TODO Create a dataframe with data from CalgaryDogBreeds.xlsx
    # TODO Do not modify the files, can change index
    
    # Import the data from the excel files `CalgaryDogBreeds.xlsx`
    dog_data_xl = pd.read_excel('CalgaryDogBreeds.xlsx')
    # Create pandas dataframe from the file
    dog_data_df = pd.DataFrame(dog_data_xl)

    # Reorganize the data to have 3 indexes `Breed, Year and Month`
    dog_data_df.set_index(['Breed', 'Year', 'Month'], inplace=True)
    # Sort the data by breed
    dog_data_df.sort_index(level=0, inplace=True)
    

    print("ENSF 692 Dogs of Calgary")

    # User input stage
    # TODO : prompt dog breed(upper case, lower case, mix case)
    
    # Create an indexSlice object that will be used to retrieve selected data
    idx0 = pd.IndexSlice

    # Create an infinite loop
    # Ask for user input and turn it directly to uppercase
    # Try to retrieve the necessary data
    # if successful break the loop
    # else raise a KeyError "Dog breed not found in the data, Please try again"

    while True:
        user_breed = input("Please enter a dog breed: ").upper()
        try:            
            # The indexSlice object uses the user_breed, all the years and all the month
            # the loc method of the dataframe slices using idx0 and all the column 
            selected_breed_data = dog_data_df.loc[idx0[user_breed,:,:],:]
            break
        except KeyError:
            print("Dog breed not found in the data. Please try again.")
        

  
    # Data analysis stage
    # one multi-index Pandas DataFrame, at least one IndexSlice object,
    # at least one masking operation, at least one grouping operation,
    # and at least one built-in Pandas or NumPy computational method.

    # TODO: Find and print all years where the selected breed was listed in the top breeds.
    
    # Create a new IndexSlice
    idx = pd.IndexSlice

    # Create the list of years where the breed reaches the top
    # From selected data, retrieves the index, then the values at index 'Year' using the get_level_index
    # call the unique method to remove duplicated object
    # and apply the tolist() method to convert into a list
    list_year = selected_breed_data.index.get_level_values('Year').unique().tolist()

    # Display the contain of list_year
    print("The", user_breed ," was found in the top breeds for years: ", *list_year)

    # TODO: Calculate and print the total number of registrations of the selected breed found in the dataset.
   
    # Apply the sum method to the column  'Total' of the selected data
    # Display the result
    total_selected_breed = selected_breed_data['Total'].sum()
    print("There have been ", total_selected_breed, user_breed, "dogs registered total.")

    # TODO: Calculate and print the percentage of selected breed registrations out of
    # the total percentage for each year (2021, 2022, 2023).
    
    # For each year in the previous list of years
    # create to indexSlice object
    # the first indexslice object helps selects the breed the total for the current year
    # the second indexSlice object helps slice the overall data including all the breeds for the current year
    for year in range(len(list_year)):
        idx2 = pd.IndexSlice
        idx3 = pd.IndexSlice
        # First idx selects user breed, the current and all the month
        # Loc method of the selected_breed_data dataframe takes the indexes (idx2) and all columns
        # The result is finally sum up
        selected_breed_year_data = selected_breed_data.loc[idx2[user_breed, list_year[year],:],:].sum()
        
        # Second idx selects all the breeds, the current and all the month
        # Loc method of the selection dataframe takes the indexes (idx3) and all columns
        # The result is finally sum up
        selected_year_data = dog_data_df.loc[idx3[:,list_year[year],:],:].sum()
        
        # Determine the percentage by dividing them
        percent_per_year = ((selected_breed_year_data / selected_year_data) * 100).iloc[0]
        print("The {0} was  {1:6f} % of tops breeds in {2}".format(user_breed, percent_per_year, list_year[year]))

    # TODO Calculate and print the percentage of selected breed registrations out of the total three-year percentage.
    # Create an other indexSlice object
    # Use it to retrieve all the index 0, all the years between the first and last year in the list of years and all the month.
    # Pass it to the loc method of the overall data(dog_data_df) to have all the breeds for those years
    # Using the total of selected breed determined above, divide by the sum of all breeds of all the years and multiply by 100
    # take the first element of the implecit index
    # Display the result
    idx4 = pd.IndexSlice
    all_selected_breed_for_all_years = dog_data_df.loc[idx4[:,list_year[0]:list_year[-1],:],:]
    percent_out_all_years = ((total_selected_breed / all_selected_breed_for_all_years.sum()) * 100).iloc[0]
    print("The {0} was {1:6f} % of tops breeds accross all years".format(user_breed, percent_out_all_years) )
    

    # TODO Find and print the months that were most popular for the selected breed registrations. Print all months that tie.

    # Group the selected data by month and sum them on total
    selected_breed_data_month = selected_breed_data.groupby('Month').sum()
    # Sort the result in descending order according to the values of 'Total', and updata the variable directly
    selected_breed_data_month.sort_values('Total', ascending=False, inplace=True)
    # Take the index of the selected_breed_data_month
    # Retrieve the level values of Month(get_level_values() function)
    # Apply the unique method to remove duplicated month and turn the result to a list
    # Display the result until the boundary of terminal.
    month = selected_breed_data_month.index.get_level_values('Month').unique().tolist()
    print("Most popular month(s) for the ", user_breed, " dogs: ", *month[:9])


if __name__ == '__main__':
    main()
