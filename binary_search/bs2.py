## Binary Search to find a key in a rotated ordered array

import numpy as np
flg = 0
def binary_search(x, start, end, key):
    while(start <= end):
        mid = start + (end - start)/2 ##To avoid overflow
        if(x[mid] == key):
            print ("Key found at position:", mid + 1)
            return
        elif(x[mid] > key):
            end = mid - 1
        elif(x[mid] < key):
            start = mid + 1
    return -1

def split(x, start, end):
    mid = start + (end - start)/2
    if (start>end):
        return -1
    if (start==end):
        return low
    if(mid<end and x[mid] > x[mid+1]):
        return mid
    elif(mid>start and x[mid] < x[mid-1]):
        return mid - 1
    elif(x[start]>=x[mid]):
        return split(x, start, mid - 1)
    else:
        return split(x, mid + 1, end)
    return


if __name__ == '__main__':
    length = int(raw_input("Enter the number of elements in the array:"))
    print "Enter the array:"
    x = np.zeros((length))
    for i in range(0, length):
         x[i] = int(raw_input("Enter the number"))
    x = x.astype(int)
    key = int(raw_input("Enter the key"))
    pivot = split(x, 0, length-1)
    print pivot
    if(key == pivot):
        print("Element found at position: ", pivot)
    elif(x[0]>key):
        binary_search(x, pivot + 1, length-1, key)
    else:
        binary_search(x, 0, pivot-1, key)
