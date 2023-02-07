import queue
import argparse
import os

class customer:

    class participant:
        __slots__= "name", "priority"
        def __init__(self,n,p):
            self.name = n
            self.priority = p
        def __it__(self,other):
            return self.name<other.name

        def is_empty(self):
            return len(self) == 0

class SortedPriorityQueue(customer):
    def __init__(self):
        self.priority = []
        self.number = []
    def __len__(self):
        return len(self.priority)
    def insert (self,n,p):

        x = ([(sub[1], sub[0]) for sub in self.priority])
        self.priority = x
        self.priority.append((p,n))
        self.priority = self.priority[::-1]

        self.priority.sort(reverse = True)

        x = ([(sub[1], sub[0]) for sub in self.priority])
        self.priority = x

def prioritize(inputFileName):
    t = []
    x = SortedPriorityQueue()
    a = open(inputFileName,"r")
    b = a.readlines()
    for line in b:
        t.append(line)
    for m in t:
        y = m.translate({ord(i): None for i in '\n'})
        e = y.translate({ord(i): None for i in '(,)'})
        number = ''.join([i for i in e if i.isdigit()])
        low = "".join([i for i in e if not i.isdigit()])
        x.insert(low,int(number))
    x.priority[0],x.priority[1] = x.priority[1],x.priority[0]
    return x

def first(queue):
    for i in queue.priority[0]:
        return i

def last(queue):
    for i in queue.priority[-1]:
        return i
def remove(queue):
    for i in queue.priority:
        if first(queue) in i:
            (queue.priority).remove(i)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description= "FileName")
    parser.add_argument('-i','--inputFileName',type=str, metavar = '', required = True)


    args = parser.parse_args()

    if os.path.isfile(args.inputFileName) == False:
        print ("File is Incorrect")

    priority = prioritize(args.inputFileName)

    print(first(priority))
    (remove(priority))
    print(first(priority))
    print(last(priority))
