# This version is for both Python 2.7.x and 3.x.x
# Name 1:
# Name 2:
# Create empty tree
def emptytree():
    return None

# Insert k into tree t
def insert(t, k):
    if t == None:
        return (k, None , None)
    else:
        key, left, right = t
        if k == key:
            return (key, left, right)
        elif k < key:
            return (key, insert(left, k), right)
        else:
            return (key, left, insert(right, k))

# Create tree by inserting each element in l into an initially empty tree
def treefromlist(l):
    t = emptytree()
    for i in range(0, len(l)):
        t = insert(t, l[i])
    return t

t1 = insert ( emptytree () , 1)
#print ( t1 ) # python 3.x.x
t2 = insert ( emptytree () , 2)
t2 = insert (t2 , 6)
t2 = insert (t2 , 7)
t2 = insert (t2 , 4)
t2 = insert (t2 , 1)
#print ( t2 ) # for python 3.x.x
# key, left, right = t2
# print(key)
# print(left)
# print(right)
