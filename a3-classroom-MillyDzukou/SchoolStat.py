class SchoolStat:
    def __init__(self, data, school_number):
        self.data = data
        self.used_data = data[:, school_number, :]

    def meanEnrol(self, grade):
        """
        This function takes a number between 10 and 12 which represents a school grade
        determine what was the mean enrollment for that grade in the current school
        """
        grade_ln = grade % 10
        return int(self.used_data[:, grade_ln].mean())

    def highestEnrol(self):
        return int(self.used_data.max())

    def lowestEnrol(self):
        return int(self.used_data.min())

    def totalEnrol(self, year):
        year_indice = year - 2013
        return int(self.used_data[year_indice, :].sum())

    def total10Enrol(self):
        return self.used_data.sum()

    def medianEnrolOver500(self):
        pass
    
    # def meanEnrol(self):
    #     pass

    def meanEnrolYearly(self):
        pass

    def totalGraduate(self):
        pass

    def higestEnrolGrade(self):
        pass

    def lowestEnrolGrade(self):
        pass


