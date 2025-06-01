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
        pass

    def lowestEnrol(self):
        pass

    def totalEnrol(self):
        pass

    def total10Enrol(self):
        pass

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


