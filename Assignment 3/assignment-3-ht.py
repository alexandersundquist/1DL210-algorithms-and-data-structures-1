# This version is for Python 3.x.x
# Name 1:
# Name 2:

import random
# Random DNA string of length 2*n

def randstring(n):
    return "".join(random.choice(["AT", "TA", "CG", "GC"]) for i in range(0, n))

# Print the hash table
def output(t):
    for k in range(0, len(t)):
        s = str(k) + ": "
        if len(t[k]) <= 30:
            for i,e in enumerate(t[k]):
                if i != 0:
                    s = s + ","
                s = s + str(e)
        else:
            s = s + "(" + str(len(t[k])) + " elements)"
        print(s)

# Construct an empty hash table with n buckets
def ht(n):
    return list(map(lambda x: [], range(n)))

# Hash function h1
def h1(e):
    return (37 * e) % 11

# Hash function h2
def h2(e):
    return (30 * e) % 8

# Hash function h3
def h3(e):
    return (e * e) % 23

# Hash function h4 (defined on strings, as the sum of all character values)
def h4(e):
    return sum(map(ord, e)) % 19

#################################
# Insert, search, delete
#################################

# Insert function
def insert (t,h,e):
    i = h(e)
    t[i].append(e)

# Search function
def search (t,h,e):
    slot = h(e)
    listslot = t[slot]
    for i in range(len(listslot)):
        if listslot[i] == e:
            return True
    return False

# Delete function
def delete (t,h,e):
    slot = h(e)
    listslot = t[slot]
    while listslot.count(e) >=1:
        listslot.remove(e)

#################################
# Test functions
#################################

def test1 ():
    t = ht(11)
    elements = 1000
    h = h1
    for i in range(elements-1):
        x = random.randint(0,elements)
        insert(t,h,x)
    output(t)

def test2():
    t = ht(8)
    elements = 1000
    h = h2
    for i in range(elements-1):
        x = random.randint(0,elements)
        insert(t,h,x)
    output(t)

def test3():
    t = ht(23)
    elements = 1000
    h = h3
    for i in range(elements-1):
        x = random.randint(0,elements)
        insert(t,h,x)
    output(t)

def test4():
    t = ht(11)
    h = h1
    insert_list = [1,12,34,45,56,67,78,89,100,111]
    for i in range(len(insert_list)):
        insert(t,h,insert_list[i])
    output(t)

def testdna():
    t = ht(19)
    h = h4
    elements = 1000
    for i in range(elements-1):
        x = randstring(10)
        insert(t,h,x)
    output(t)

def testquadratic():
    print('Iteration, quadratic, rest' )
    for i in range(100):
        print(i, ' : ', i**2, ' : ' ,i**2 % 23)

#test1()
#test2()
#test3()
#test4()
#testdna()
#testquadratic()
