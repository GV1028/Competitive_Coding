## Program to find floor and ceil of given number using binary search

import numpy as np

def ceilfunc(x, start, end, key):
    if(key < x[start]):
        return x[start]
    if(key > x[end]):
        return -1
    mid = start + (end - start)/2 ##To avoid overflow
    if(x[mid] == key):
        return x[mid]
    elif(x[mid] < key):
        if(mid + 1 <= end and x[mid + 1] >= key):
            return x[mid + 1]
        else:
            return ceilfunc(x, mid + 1, end, key)
    else:
        if(mid - 1 >= start and x[mid - 1] < key):
            return x[mid]
        else:
            return ceilfunc(x, start, mid - 1, key)
    return

def floorfunc(x, start, end, key):
    if(key < x[start]):
        return -1
    if(key > x[end]):
        return x[end]
    mid = start + (end - start)/2 ##To avoid overflow
    if(x[mid] == key):
        return x[mid]
    elif(x[mid] < key):
        if(mid + 1 <= end and x[mid + 1] <= key):
            return x[mid + 1]
        else:
            return floorfunc(x, mid + 1, end, key)
    else:
        if(mid - 1 >= start and x[mid - 1] > key):
            return x[mid]
        else:
            return floorfunc(x, start, mid - 1, key)
    return

if __name__ == '__main__':
    length = int(raw_input("Enter the number of elements in the array:"))
    print "Enter the array:"
    x = np.zeros((length))
    for i in range(0, length):
         x[i] = int(raw_input("Enter the number"))
    x = x.astype(int)
    key = int(raw_input("Enter the key"))
    print floorfunc(x, 0, length-1, key)
