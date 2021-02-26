# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, year= '', classes= ''):
        self.name = name
        self.gpa = gpa
        self.year = year
        self.enrolled = classes
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
    
    def get_gpa(self):
        return self.gpa
        
    def set_year(self,year):
        self.year = year
        return 
    
    def get_year(self):
        return self.year

    def set_enrolled(self, classes):
        self.enrolled = classes
        return 
    
    def get_enrolled(self):
        return self.enrolled
    
        
    def display_courses(self):
        print("I am enrolled in", self.enrolled)
        
    def year_until_graduation(self):
        grad_years = 4 - self.year
        print("I will graduate in",grad_years,"years")
        
        
class Spartan():
    def __init__(self, name='', motto = ""):
        self.name = name
        self.motto = motto  
        
    def school_spirit(self):
        print("My name is", self.name, ".","I am a Spartan. My motto is",self.motto)
    
    
