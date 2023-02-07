from MyDataStructures2  import Stack
import argparse
import sys
import os.path
import csv
def push_2 (file,objec):
    t = []
    a = open(file, "r")
    b = csv.reader(a)
    for line in b:
        for i in line:
            c = int(i)
            t.append(c)
    for i in t:
        objec.push(i)
    return objec

def reverse(stack):
    r = ""
    for i in range(stack.__len__()):
        x = stack.pop()
        z = str(x)
        r+=z
    for i in range(len(r)):
        f = int(r[i])
        stack.push(f)
    if r == r[::-1]:
        return True
    else:
        return False

def inverse(stack):
    t = []
    for i in range(stack.__len__()):
        i = i-1
        x = stack.pop()
        t.append(x)
    for i in t:
        stack.push(i)

def count (stack):
    x = stack.__len__()
    t = []
    for i in range(x):
        v = stack.pop()
        t.append(v)
    r = sum(t)

    return x,r

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description= "FileName")
    parser.add_argument('-i','--inputFileName',type=str, metavar = '', required = True)

    args = parser.parse_args()

    if os.path.isfile(args.inputFileName) == False:
        print ("File is Incorrect")
    objec = Stack()
    stack =  push_2 (args.inputFileName,objec)
    objec.push(1)
    objec.pop()
    x = reverse(objec)
    print(x)
    objec.push(1)
    objec.pop()
    z = inverse(objec)
    print(x)
    print(objec.top())
    y = count(objec)
    print(y)
