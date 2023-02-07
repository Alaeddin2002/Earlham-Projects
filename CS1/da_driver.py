import sys
import os.path
import csv
from dynamic_array import DynamicArray

def populate(inputFileName):
    t = []
    r = DynamicArray()
    a = open(inputFileName,"r")
    b = csv.reader(a)
    for line in b:
        for i in line:
            object = int(i)
            t.append(object)
    for i in t:
        r.append(i)
    return r


def displayUnique(myArray):
    t = []
    k = []
    for i in range(myArray.__len__()):
        x = myArray.__getitem__(i)
        t.append(x)
        new = set(t)
    for j in new:
        k.append(j)
        k.sort()
    for i in k:
        print (i)

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description='Lab 5 - arrays')
	parser.add_argument('-i','--inputFileName', type=str, help='File of integers, one per line', required=True)
	args = parser.parse_args()

	if not (os.path.isfile(args.inputFileName)):
		print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
		exit(-1)
	function = populate(args.inputFileName)
	display = displayUnique(function)
	print(function.__getitem__(-15))
	x = function._n
	(function.removeAll(7))
	print(function.__getitem__(-15))
	for i in range (x):
		function.insertEfficient(0,7)
