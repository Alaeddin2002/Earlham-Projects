import math
import argparse
import csv
import os

class Student:
    def __init__(self,ID, firstName, lastName, email, year, gpa):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.year = year
        self.gpa = gpa

    def get_ID(self):
        if self.ID == int(self.ID) and 9999>=self.ID >=0:
            return self.ID
        else:
            return "ID is not a whole positive number"

    def set_ID(self,new_ID):
        self.ID = new_ID

    def get_firstName(self):
        if self.firstName == str(self.firstName):
            return self.firstName
        else:
            return "First Name is not a string"

    def set_firstName(self, new_firstName):
        self.firstName = new_firstName

    def get_lastName(self):
        if self.lastName == str(self.lastName):
            return self.lastName
        else:
            return "Last Name is not a string"

    def set_lastName(self, new_lastName):
        self.lastName = new_lastName

    def get_email(self):
        if self.email[-1] == "u" and self.email[-2] == "d" and self.email[-3] == "e" and self.email[-4] == ".":
            return self.email
        else:
            return "email is invalid"
        return self.email

    def set_email(self, new_email):
        self.email = new_email

    def get_year(self):
        if self.year =="SO" or "JR" or "SR" or "FR":
            return self.year
        else:
            return "Year is invalid"

    def set_year(self, new_year):
        self.year = new_year

    def get_gpa(self):
        if self.gpa == int(self.gpa) and 5>self.gpa>0:
            return self.gpa
        elif self.gpa == float(self.gpa) and 5>self.gpa>0:
            return self.gpa
        else:
            return "GPA is not a positive number or a correct value"

    def set_gpa(self,new_gpa):
        self.gpa = new_gpa

def loadStudents(inputFileName):
    t = []
    k = []
    a = open (inputFileName,"r")
    b = a.readlines()
    for line in b:
        t.append (line)

    for i in t:
        if i[0].isdigit():
            r = Student(i[0],i[1],i[2],i[3],i[4],i[5])
            k.append(r)
    return k


def displayStudents(studentArray):
    for i in studentArray:
        print (i.get_ID() , "," , i.get_firstName(), "," , i.get_lastName() , "," , i.get_email() , "," , i.get_year(),",", i.get_gpa())

def averageGPA(studentArray):
    l = []
    for i in studentArray:
        e = i.get_gpa()
        l.append(e)

    c = len(l)
    t = sum(l)
    y = round(t/c,2)
    print(y)


def improveGPA(studentArray, percentImprovement = 1):
    l = []
    for i in studentArray:
        e = i.get_gpa()
        l.append(e)

    for j in l:
        j + percentImprovement
        if j+percentImprovement >4.0:
                i.set_gpa(4.0)
        else:
             i.set_gpa(j+percentImprovement)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description= "FileName and GPA addition")
    parser.add_argument('-i','--inputFileName',type=str,metavar = '', required = True)
    parser.add_argument('-p','--percentImprovement',type=int, metavar = '', required = True)
    args = parser.parse_args()

    if os.path.isfile(args.inputFileName) == False:
        print ("File is Incorrect")
    if args.percentImprovement != int(args.percentImprovement):
        print ("Number is not an integer")

    filename = loadStudents(args.inputFileName)
    gpa_addition = improveGPA(filename,args.percentImprovement)
    print(filename)
    print(DisplayStudents(filename))
    print(averageGPA(filename))
    gpa_addition
    print(filename.get_gpa())
