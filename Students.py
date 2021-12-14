class person:
    def __init__(self,name="",address=""):
        self.__name = name
        self.__address = address
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def setAdress(self,address):
        self.address = address
    def __str__(self):
        return "student:{} ({})".format(self.__grades, self.__courses, self.__numCourse)

class student(person):
    def __init__(self,numCourse = 0, courses="", grades=""):
        self.__numCourse = 0
        self.__courses = []
        self.__grades = []
    def addCourseGrade(self,course,grade):
        self.__courses = course
        self.__grades = int(grade)
    def printGrades(self):
        print(self.__grades)
    def getAvarageGrades(self):
        formula = sum(self.__grades) / len(self.__grades)
        print("Your Average grade is".format(formula))
    def __str__(self):
        return "student:{} ({})".format(self.__grades, self.__courses, self.__numCourse)

class teacher(person):
    def __init__(self,numCourse = 0, course=""):
        self.__numCourse = 0
        self.__course = []
    def addCourse(self,course):
        
        