from MyDataStructures2 import queue
import argparse
import sys
import os.path
import csv
def enqueue_1 (file,objec):
    t = []
    a = open(file, "r")
    b = csv.reader(a)
    for line in b:
        for i in line:
            t.append(i)
    for i in t:
        v = int(i)
        objec.enqueue(v)
    return objec

def reverse (queue):
    r = ""
    for i in range(queue.__len__()):
        x = queue.dequeue()
        z = str(x)
        r+=z
        queue.enqueue(x)
    if r == r[::-1]:
        return True
    else:
        return False

def inverse(queue):
    t = []
    for i in range(queue.__len__()):
        i = i-1
        x = queue.dequeue()
        t.append(x)
    for i in t:
        queue.enqueue(i)

def count (queue):
    x = queue.__len__()
    t = []
    for i in range(x):
        v = queue.dequeue()
        t.append(v)
    r = sum(t)

    return (x,r)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description= "FileName")
    parser.add_argument('-i','--inputFileName',type=str, metavar = '', required = True)

    args = parser.parse_args()

    if os.path.isfile(args.inputFileName) == False:
        print ("File is Incorrect")
    objec = queue()
    queue =  enqueue_1 (args.inputFileName,objec)
    v = objec.dequeue()
    objec.enqueue(v)
    x = reverse(objec)
    print(x)
    f = objec.dequeue()
    objec.enqueue(f)
    z = inverse(objec)
    print(x)
    print(objec.front())
    y = count(objec)
    print(y)
