'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''

def movezeros(arr): # this method does not maintain order of elements in array
    if len(arr)==0:
        return -1
    i=0
    j=len(arr)-1

    while(i<j):
        if arr[i]==0 and arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        elif arr[i]==0:
            j-=1
        else:
            i+=1
    return arr

def movezeros_maintainorder(arr):
    if len(arr)==0:
        return -1
    i=0
    j=1

    while( j <len(arr)):
        if arr[i]!=0 and arr[j]==0:
            arr[i],arr[j]=arr[j],arr[i]
        elif j<=i or arr[j]==0:
            i+=1
        else:
            j+=1
    return arr



arr=[0,1,0,3,12,0]
print("Order Not Maintained:")
print(movezeros(arr))

arr1=[0,1,0,3,12,0,0,0,0]
print("======================")
print("Order Maintained:")
print(movezeros_maintainorder(arr1))


