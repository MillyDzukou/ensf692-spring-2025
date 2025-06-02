import numpy as np

class SchoolStat:
    """
    This class contains the core of program. It is designed to provide
    all the single functions that will manipulate our data and return
    useful statistic.

    Attributes:
        data (np.array): provide the class with you data.
        school_number (int): is the integer representing the school
        index choosen by the user inside our program.
        used_data(np.array): represents the data from the chosen
        school ony.

    """
    def __init__(self, data, school_number):
        self.data = data
        self.used_data = data[:, school_number, :]

    def mean_enrol(self, grade):
        """
        mean_enrol takes a number between 10 and 12 which represents a school grade
        and determine what was the mean enrollment for that grade in the chosen school.

        Attributes:
            grade (integer): the school grade between 10 and 12

        return
            int: mean enrollment inside that grade
        """
        grade_ln = grade % 10   # Determine the indice between 0, 1 or 2 of the grade.

        # extract the data for the grade from used_data
        # call the mean function
        # and call the int function to round the result.
        return int(self.used_data[:, grade_ln].mean())

    def highest_enrol(self):
        """
        highest_enrol function determine the maximum number of
        enrollment in a grade in the current school
        
        """
        return int(self.used_data.max())

    def lowest_enrol(self):
        """
        lowest_enrol function determine the minimum number of
        enrollment in a grade in the current school
        
        """
        return int(self.used_data.min())

    def total_enrol(self, year):
        """
        total_enrol determine the total enrollment for a year
        regardeless of the grade.

        Attributes:
            year(integer): year that user want the total enrollment

        return:
            int : total Enrollment for year
        """
        year_indice = year - 2013 # Determine the index of year inside the data

        # from used_data extract the data concerning only year
        # sum it
        # round with the int function
        return int(self.used_data[year_indice, :].sum())

    def total_ten_enrol(self):
        """
        total_ten_enrol determine the total of enrollment
        during all the years regardless of the grade.

        """

        # apply sum function on used_data
        return int(self.used_data.sum())

    def mean_enrol_ten(self):
        """
        mean_enrol_ten determines the mean enrollment of all the years
        for all the grade in a school.
        """

        # from used_data appy sum along the axis 1(grade axis)
        # then apply the mean
        # finally round the result with the int function.
        return  int(np.sum(self.used_data, axis=1).mean()) # int(np.sum(self.used_data, axis=0))    

    def median_enrol_over_500(self):
        """
        median_enrol_over_500 determines median number of enrollment regardless
        of the grade and if only the reach 500 enrollments that year.
        """
        # Create a mask that will be use to determine which value will be use in calculation
        mask = self.used_data > 500
        
        # Checks if the mask contains at least one positive value.
        if not mask.sum(): return "No enrollments over 500."

        # from the used_data apply the mask
        # call the median function
        # round the result using the int function.
        return int(np.median(self.used_data[mask]))
    
        
    def mean_enrol_yearly(self, year):
        """
        mean_enrol_yearly determines for all the school the mean of enrollment
        for a year regardless of the grade.
        Attributes:
            year(integer): The given year 
        """
        # Find the index the year inside our data
        year_indice = year - 2013

        # From the data(overall data) select the given year
        # apply np,nanmean (which ignore all the NaN values)
        # round the result with int function.
        return int(np.nanmean(self.data[year_indice, :, :]))

    def total_graduate(self,year):
        """
        total_graduate determines the total of graduated for a given year.

        Attributes:
            year (integer): given year.
        """
        # Find the index the year inside our data
        year_indice = year - 2013

        # From data extract the given year and the grade 12 (last index)
        # apply nansum to sum while ignoring the NaN values
        # round the final result
        return int(np.nansum(self.data[year_indice, :,2])) 
    
    def highest_enrol_grade(self):
        """
        Determine the maximum of enrolment for a grade over the 10 years in
        all the schools.
        """
        return int(np.nanmax(self.data))

    def lowest_enrol_grade(self):
        """
        Determine the minimum of enrolment for a grade over the 10 years in
        all the schools."""
        return int(np.nanmin(self.data))


