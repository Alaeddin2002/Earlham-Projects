import argparse
from string import digits
import os
import csv
class LinkedList:

    class Node:
        __slots__ = 'domain','reference','pointer'

        def __init__(self,domain,reference,pointer):
            self.domain = domain
            self.reference = reference
            self.pointer = pointer



    def __init__(self):
        self.head_pointer = None
        self._size = 0
        self.tail= None
        self.reference_2 = []
        self.unique = 0
        self.popular = []

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size ==0

    def push(self,domain,reference):
        self.head_pointer = self.Node(domain,reference,self.head_pointer)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty ("Stack is empty")
        return self.head_pointer.domain, self.head_pointer.reference
    def pop(self):
        if self.is_empty():
            raise Empty ("Stack is empty")
        answer = self.head_pointer.domain, self.head_pointer.reference
        self.head_pointer = self.head_pointer.pointer
        self._size -=1
        return answer

    def sume(self):
        return sum(self.reference_2)
    def mostpopular(self):
        for i in range (len(self.reference_2)):
            if self.reference_2[i] == max(self.reference_2):
                print (self.popular[i],self.reference_2[i])
    def percentage (self):
        print((max(self.reference_2)/sum(self.reference_2)) * 100,"%")



def website(inputFile):
    t = []
    g = []
    k = []
    c = []
    d = []
    r = LinkedList()
    a = open(inputFile,"r")
    b = csv.reader(a)
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
        r.head_pointer = r.Node(i[0],t.count(i[0]),r.head_pointer)
        if i != i[0]:
            second = r.push(i,t.count(i))
            k.append(t.count(i))
            r.head_pointer.pointer = second
            if t.count(i) == 1:
                c.append(t.count(i))
                if t.count(i) == max(c):
                    d += (i,t.count(i))
    r.reference_2 += k
    r.unique += len(x)
    r.popular += x


    return r


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description= "FileName")
    parser.add_argument('-i','--inputFileName',type=str, metavar = '', required = True)

    args = parser.parse_args()

    if os.path.isfile(args.inputFileName) == False:
        print ("File is Incorrect")

    Domain = website(args.inputFileName)
    print(Domain.sume())
    print(Domain.unique)
    (Domain.popular)
    (Domain.mostpopular())
    (Domain.percentage())
