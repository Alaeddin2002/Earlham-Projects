import math
import argparse
parser=argparse.ArgumentParser(description= "FileName and GPA addition")
parser.add_argument('-s','--inputFileName',type=str, metavar = '', required = True)
parser.add_argument('-e','--inputFileName',type=str,metavar = '', required = True)
parser.add_argument('-a','--studentArray',type=list, metavar = '', required = False)
parser.add_argument('-d','--inputFileName',type=str, metavar = '', required = True)
args = parser.parse_args()
class Student:

    def __init__(self, studentType,firstName, lastName, ID, email):

        self.studentType = studentType
        self.firstName =firstName
        self.lastName = lastName
        self.ID = ID
        self.email = email

    def getstudentType(self):
        if self.studentType == "under":
            return self.studentType

        if self.studentType == "grad":
            return self.studentType
        else:
            return "Student Type must be under or grad"

    def setstudentType (self):
        self.studentType = studentType


    def getfirstName(self):
        if self.firstName == str(self.firstName):
            return self.firstName
        else:
            return "First Name is not a string"

    def setfirstName (self):
        self.firstName = firstName

    def getlastName(self):
        if self.lastName == str(self.lastName):
            return self.lastName
        else:
            return "Last Name is not a string"

    def setlastName (self):
        self.lastName = lastName

    def getID(self):
        if self.ID == int(self.ID):
            return self.ID
        else:
            return "ID is not a whole positive number"

    def setID (self):
        self.ID = ID

    def getemail(self):
        if self.email[-1] == "u" and self.email[-2] == "d" and self.email[-3] == "e" and self.email[-4] == ".":
            return self.email
        else:
            return "email is invalid"

    def setemail (self):
        self.email = email

class Undergraduate (Student):

    def __init__(self, studentType,firstName, lastName, ID, email,dormRoom):
        super().__init__(studentType,firstName, lastName, ID, email)
        self.dormRoom = dormRoom

    def getdormRoom(self):
        for i in self.dormRoom:
            if any(map(str.isdigit, self.dormRoom[-1])) and any(map(str.isdigit, self.dormRoom[-2])) and any(map(str.isdigit, self.dormRoom[-3])):
                return self.dormRoom
            else:
                return "Dorm Room inserted is incorrect"
    def setdormRoom(self):
        self.dormRoom = dormRoom

class Graduate (Student):

    def __init__(self, studentType,firstName, lastName, ID, email,office):
        super().__init__(studentType,firstName, lastName, ID, email)
        self.office = office

    def getoffice(self):
        for i in self.office:
            if any(map(str.isdigit, self.office[-1])) and any(map(str.isdigit, self.office[-2])) and any(map(str.isdigit, self.office[-3])):
                return self.office
            else:
                return "Dorm Room inserted is incorrect"
    def setoffice(self):
        self.office = office

x = Graduate("under","Ihsan","Alaeddin",653,"earlham.edu","eret543")
x.getemail()

class Course():

    def __init__(self, department,number, enrolledIDList):

        self.department = department
        self.number = number
        self.enrolledIDList = enrolledIDList

    def getdepartment(self):
        if self.department == str(self.department):
            return self.department
        else:
            return "department name is wrong"
    def setdepartment(self):
        self.department = department

    def getnumber(self):
        if self.number == int(self.number):
            return self.number
        else:
            return "number is a string"

    def setnumber(self):
        self.number = number

    def getenrolledIDList(self):
        for i in range (len(self.enrolledIDList)):
            if str(self.enrolledIDList[i]).isdigit():
                if self.enrolledIDList == list(self.enrolledIDList):
                    return self.enrolledIDList

            else:
                return "ID list is not a list or digits"

    def setenrolledIDList(self):
        self.enrolledIDList = enrolledIDList


    def enrollStudent(self,studentID):

        if studentID in self.enrolledIDList:
            return ("ID is correct")

        else:
            return "ID is incorrect"



    def  countStudents(self):
        len(self.enrolledIDList)


    def dropStudent(self,studentID):
        self.enrolledIDList.remove(studentID)
        return self.enrolledIDList

    def dropStudents(self,inputFileName):
        t = []
        a = open (inputFileName, "r+")
        b = a.readlines()
        for line in b:
            t.append (line.strip())
        for i in range (len(t)):
            i = 0
            t.remove(t[i])
        if t == []:
            a.write("\n")



def loadStudents(inputFileName):
    t = []
    a = open (inputFileName,"r")
    b = a.readlines()
    for line in b:
        t.append (line.strip())
    return t

def enrolling(inputFileName, studentArray):

    a = open (inputFileName,"w")
    x = str(studentArray)

    for i in range(len(studentArray)):
        if str(studentArray[i]).isdigit():
            if studentArray == list(studentArray):
                a.write(str(studentArray[i]))
                a.write("")
        else:
            return "ID is not a digit"

if __name__ == '__main__':
    studentfilename = loadStudents(args.inputFileName)
    coursefilename = enrolling(args.inputFileName,args.studentArray)
    dropcourse = dropStudents(args.inputFileName)
