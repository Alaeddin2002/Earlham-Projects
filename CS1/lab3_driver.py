import math
import argparse
import os
import csv


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

    def setstudentType (self, new_studentType):
        self.studentType = new_studentType


    def getfirstName(self):
        if self.firstName == str(self.firstName):
            return self.firstName
        else:
            return "First Name is not a string"

    def setfirstName (self,new_firstName):
        self.firstName = new_firstName

    def getlastName(self):
        if self.lastName == str(self.lastName):
            return self.lastName
        else:
            return "Last Name is not a string"

    def setlastName (self,new_lastName):
        self.lastName = new_lastName

    def getID(self):
        if self.ID.is_integer():
            return self.ID
        else:
            return "ID is not a whole positive number"

    def setID (self,new_ID):
        self.ID = new_ID

    def getemail(self):
        if self.email[-1] == "u" and self.email[-2] == "d" and self.email[-3] == "e" and self.email[-4] == ".":
            return self.email
        else:
            return "email is invalid"

    def setemail (self,new_email):
        self.email = new_email

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
    def setdormRoom(self,new_dormRoom):
        self.dormRoom = new_dormRoom

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
    def setoffice(self,new_office):
        self.office = new_office


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
    def setdepartment(self,new_department):
        self.department = new_department

    def getnumber(self):
        if self.number == int(self.number):
            return self.number
        else:
            return "number is a string"

    def setnumber(self,new_number):
        self.number = new_number

    def getenrolledIDList(self):
        for i in range (len(self.enrolledIDList)):
            if str(self.enrolledIDList[i]).isdigit():
                if self.enrolledIDList == list(self.enrolledIDList):
                    return self.enrolledIDList

            else:
                return "ID list is not a list or digits"

    def setenrolledIDList(self,new_enrolledIDList):
        self.enrolledIDList = new_enrolledIDList


    def enrollStudent(self,studentID):

        self.enrolledIDList.append(studentID)
        return self.enrolledIDList


    def  countStudents(self):
        x = len(self.enrolledIDList)
        return x


def loadStudents(inputFileName):
    t = []
    k = []
    a = open (inputFileName,"r")
    b = csv.reader(a)
    for line in b:
        t.append (line)

    for i in t:
        if i[0] == "grad":
            r = Graduate(i[0],i[2],i[3],i[1],i[4],i[5])
            k.append(r)
        elif i[0] == "under":
            f = Undergraduate(i[0],i[2],i[3],i[1],i[4],i[5])
            k.append(f)
    return k


def enrolling(inputFileName, studentArray):
    l = []

    a = open (inputFileName,"r")
    b = a.readlines()
    x = str(studentArray)
    p = Course("CS",256, l )
    for i in range(len(studentArray)):
        if isinstance(studentArray[i],int):
            p.enrollStudent(studentArray[i])
        else:
            continue
    return p


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description= "FileName")
    parser.add_argument('-s','--inputFileName',type=str, metavar = '', required = True)
    parser.add_argument('-e','--inputFileName1',type=str,metavar = '', required = True)


    args = parser.parse_args()

    if os.path.isfile(args.inputFileName) == False:
        print ("File is Incorrect")
    if os.path.isfile(args.inputFileName1) == False:
        print ("File is Incorrect")

    student_list = loadStudents(args.inputFileName)
    course = enrolling(args.inputFileName1,student_list)
    print (course.countStudents())
