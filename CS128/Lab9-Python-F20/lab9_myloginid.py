def find ():
    x = 'AACCTTNN'
    a = open("first")
    b = open("fourth", 'w')
    c = open ("second")
    for line in a: 
        if x in line: 
            b.write(line + '\n') 
    for line in c: 
        if x in line: 
            b.write(line + '\n') 
    a.close()
    c.close()
    
find()          
    