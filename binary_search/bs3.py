##Program to check if the given element appears more than n/2 times in an array

import numpy as np

def binary_search(x, start, end, key):
    while(start <= end):
        mid = start + (end - start)/2 ##To avoid overflow
        if((mid == 0 or x[mid - 1] < key) and x[mid] == key):
            return mid
        elif(x[mid] < key):
            start = mid + 1
        else:
            end = mid - 1
    return

def isMajority(x, key, start, end):
    firstpos = binary_search(x, start, end, key)
    print firstpos
    if(firstpos + end/2 <= end):
        if(x[firstpos + end/2] == key):
            return True
    return False


if __name__ == '__main__':
    length = int(raw_input("Enter the number of elements in the array:"))
    print "Enter the array:"
    x = np.zeros((length))
    for i in range(0, length):
         x[i] = int(raw_input("Enter the number"))
    x = x.astype(int)
    key = int(raw_input("Enter the key"))
    print isMajority(x, key, 0, length-1)
