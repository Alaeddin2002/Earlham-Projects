import os
import argparse
from string import digits
import csv
class Node:

    def __init__(self,domain,reference):

        self.left = None
        self.right = None
        self.parent = None
        self.domain = domain
        self.reference = reference

    def getdomain(self):
        return self.domain

    def setdomain(self,new_domain):
         self.domain == new_domain

    def getreference(self):
        return self.domain

    def setreference(self,new_reference):
         self.reference == new_reference





class binary_search_tree():

    def __init__(self):
        self.root = None

    def addOrIncrementDomainNameNode(self,domain,reference = 1):
        if self.root == None:
            self.root = Node(domain,reference)

        else:
            self._addOrIncrementDomainNameNode(domain, reference, self.root)
    def _addOrIncrementDomainNameNode(self,domain, reference,cur_Node):
        if domain < cur_Node.domain:
            if cur_Node.left == None:
                cur_Node.left == Node(domain,reference)
            else:
                self.__addOrIncrementDomainNameNode(domain,cur_Node.left)

        elif domain > cur_Node.domain:
            if cur_Node.right == None:
                cur_Node.right == Node(domain,reference)
            else:
                self.__addOrIncrementDomainNameNode(domain, cur_Node.right)
        else:
             self.root = (Node(domain,reference+1))



    def PrintTree(self):
        if self.root !=None:
            self._PrintTree(self.root)


    def _PrintTree(self, cur_Node):
        if cur_Node != None:
            self._PrintTree(cur_Node.left)
            x =  (str(cur_Node.domain))
            c =  (str(cur_Node.reference))
            print(x,c)
            self._PrintTree(cur_Node.right)

def domains(inputFileName):
    t = []
    k = []
    c = []
    d = []
    a = open(inputFileName,"r")
    b = csv.reader(a)
    r = binary_search_tree()
    for line in b:
        for i in line:
            z = i.split()
            p = str.maketrans('', '',digits)
            u = z[0].translate(p)
            y = u.replace(":","")
            if "edu" in y:
                t.append(y)
    x = set(t)
    for i in x:
        if t.count(i) == 1:
            r.addOrIncrementDomainNameNode(i)
        if t.count(i) > 1:
            r.addOrIncrementDomainNameNode(i,t.count(i))




    return r

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description= "FileName")
    parser.add_argument('-i','--inputFileName',type=str, metavar = '', required = True)


    args = parser.parse_args()

    if os.path.isfile(args.inputFileName) == False:
        print ("File is Incorrect")

    websites = domains(args.inputFileName)
    websites.PrintTree()
