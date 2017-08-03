## Binary search to find a key in shortest number of comparisons
import numpy as np

def binary_search(x, start, end, key):
    while(start <= end):
        mid = (start + end)/2
        if(x[mid] == key):
            print ("Key found at position:", mid + 1)
            return
        elif(x[mid] > key):
            end = mid - 1
        elif(x[mid] < key):
            start = mid + 1
    return

if __name__ == '__main__':
    length = int(raw_input("Enter the number of elements in the array:"))
    print "Enter the array:"
    x = np.zeros((length))
    for i in range(0, length):
         x[i] = int(raw_input("Enter the number"))
    x = x.astype(int)
    print x
    key = int(raw_input("Enter the key"))
    print key
    binary_search(x, 0, length-1, key)
