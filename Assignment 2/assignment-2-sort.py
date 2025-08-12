import os
import array
import sys
import math
import time

# Bubble Sort Implementation

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def bubblesort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                sorted = False

def run_bubblesort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing bubblesort
    bubblesort(a)

    # output nums_sorted.txt
    nums_sorted = open('bubblesorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")
    nums.close()
    nums_sorted.close()

# Merge Sort Implementation
def merge(a,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    l = []
    m = []
    i = 1
    j = 1
    while i < n1+1:
        l.append(a[p+i-1])
        i += 1
    while j < n2+1:
        m.append(a[q+j])
        j += 1
        l.append(math.inf)
        m.append(math.inf)
        i = 0
        j = 0
        k = p
    while k < r+1:
        if l[i] <= m[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = m[j]
            j += 1
            k += 1

def mergesort(a,p,r):
    if p < r:
        q = (p+r)//2
        mergesort(a,p,q)
        mergesort(a,q+1,r)
        merge(a,p,q,r)

def run_mergesort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing mergesort
    # Call your mergesort implementation here
    p = 0
    r = len(a)-1
    mergesort(a,p,r)

    # output nums_sorted.txt
    nums_sorted = open('mergesorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

# Quick Sort Implementation
def partition(a,p,r):
    x = a[r]
    i = p - 1
    j = p
    while j < r:
        if a[j] <= x:
            i += 1
            swap(a,i,j)
            j += 1
        swap(a,i+1,r)
        return i + 1
    
def quicksort(a,p,r):
    if p < r:
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)

def run_quicksort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing quicksort
    # Call your quicksort implementation here
    p = 0
    r = len(a)-1
    quicksort(a,p,r)

    # output nums_sorted.txt
    nums_sorted = open('quicksorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

# Heap Sort Implementation
def max_heapify(a,i,heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= heapsize-1 and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize-1 and a[r] > a[largest]:
        largest = r
    if largest != i:
        swap(a,i,largest)
        max_heapify(a,largest,heapsize)

def build_max_heap(a):
    heapsize = len(a)
    i = len(a)//2
    while i >= 0:
        max_heapify(a,i,heapsize)
        i -= 1

def heapsort(a):
    heapsize = len(a)
    build_max_heap(a)
    i = len(a)-1
    while i > 0:
        swap(a,0,i)
        heapsize -= 1
        max_heapify(a,0,heapsize)
        i -= 1

def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing heapsort
    # Call your heapsort implementation here
    heapsort(a)

    # output nums_sorted.txt
    nums_sorted = open('heapsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print ("First create nums.txt")
        sys.exit(0)

    run_bubblesort()
    run_mergesort()
    run_quicksort()
    run_heapsort()

# python sort.py runs run
if __name__ == "__main__":
    run()