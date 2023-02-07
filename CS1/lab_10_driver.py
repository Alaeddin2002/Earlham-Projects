import argparse
import os
import csv
class books:
    def __init__ (self):
        self.checkouts = []
        self.checkin = []
        self.copy = []
        self.books = []

    def __len__(self):
        return len(self.books)
    def addBook (self,title,ISBN,copies = 1):
        if title is not int:
            if (title,ISBN) not in self.books:
                self.books.append((title,ISBN))
                self.copy.append(copies)
            else:
                for i in range (len(self.books)):
                    if self.books[i] == (title,ISBN):
                        self.copy[i] = self.copy[i]+1


    def removeBook(self,title,ISBN,copies = 1):
        if (title,ISBN) in self.books:
            for i in range (len(self.books)-1):
                if self.books[i] == (title,ISBN):
                    self.copy[i] = self.copy[i]-copies

        else:
            return "title or ISBN is invalid"
    def frequency(self):
        r = []
        for i in range (len(self.checkouts)):
            c = max(self.checkouts)
            if c == self.checkouts[i]:
                    x = self.books[i]
            for i in x:
                r.append(i)
        print (r[1], ",",r[0], ",",c)
    def occurences(self):
        self.books.remove(self.books[-1])
        self.copy.remove(self.copy[-1])


class customer():
    def __init__(self):
        self.patrons = []
        self.patron_checkout = []
    def addPatron (self,patron):
        if patron is not str:
            self.patrons.append(patron)
        else:
            return "must be a number"
    def removePatron(self,patron):
        if patron in self.patrons:
            self.patrons.remove(patron)
        else:
            return "patron is invalid"
    def file (self,inputFileName):
        t = []
        c = []
        r = []
        f = books()
        a = open (inputFileName,"r")
        b = csv.reader(a)
        for line in b:
            for i in line:
                if "addPatron" == i:
                    self.addPatron (int(line[1]))
                    self.patron_checkout.append(0)
                if "removePatron" == i:
                    self.removePatron (int(line[1]))
                if "addBook" == i:
                    z = (line[1])
                    f.addBook (line[2],z)
                if "removeBook" == i:
                    d = (line[1])
                    for i in range(len(f.books)-1):
                        if b in f.books[i]:
                            for k in f.books[i]:
                                if k is not int:
                                    f.removeBook (k,d)
                if "checkout" == i:
                    d = (line[1])
                    b = line[2]
                    for i in self.patrons:
                        if i == int(d):
                            for i in range(len(f.books)-1):
                                if b in f.books[i]:
                                    for k in f.books[i]:
                                        if k is not int:
                                            checkout(d,k,line[2],f)
                    f.checkouts.append(1)
                    for i in range(len(self.patrons)):
                        if self.patrons[i] == int(d):
                            self.patron_checkout[i] = self.patron_checkout[i] +1


                if "checkin" == i:
                    d = (line[2])
                    for i in range(len(f.books)):
                        if d in f.books[i]:
                            for k in f.books[i]:
                                if k is not int:
                                    checkin(k,d,f)
                    f.checkin.append(1)

        return f
    def active(self):
        r = []
        for i in range (len(self.patron_checkout)):
            c = max(self.patron_checkout)
            if c == self.patron_checkout[i]:
                print (self.patrons[i], ",", c)

def checkout(patron,book,ISBN, library):
    if (book,ISBN) in library.books:
        library.removeBook(book,ISBN)





def checkin(book,ISBN,library):
    library.addBook(book,ISBN)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description= "FileName")
    parser.add_argument('-i','--inputFileName',type=str, metavar = '', required = True)


    args = parser.parse_args()

    if os.path.isfile(args.inputFileName) == False:
        print ("File is Incorrect")

    x = customer()
    filename = x.file(args.inputFileName)
    print(filename)
    filename.occurences()
    print(len(filename.copy))
    print(sum(filename.checkouts))
    print(sum(filename.checkin))
    ((filename.frequency()))
    ((x.active()))
