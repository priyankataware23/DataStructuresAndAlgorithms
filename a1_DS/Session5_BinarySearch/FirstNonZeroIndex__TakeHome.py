'''
Q1
Given an array with 0(s) at the left and 1(s) at the right, find position of the last zero in the array.

arr=[0,0,0,0,1,1,1,1]
output=3
 approach 2 pointer, where j is always ahead of i
'''

def returnNonZeroPosition(arr):
    if arr== None:
        return -1
    if len(arr)==1:
        return -1
    i=0
    j=1
    while(i<j):
        if arr[i]==arr[j]:
            i+=1
            j+=1
        else:
            return i
    return -1

arr=[0,0,0,0,1,1,1,1]
print (returnNonZeroPosition(arr))


#-- below is using binar search
def returnLast0index(arr):
    if not arr:
        return "Empty Array"
    lo=0
    hi=len(arr)-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if arr[mid]==0 and (mid+1 <= len(arr)-1 or arr[mid+1]!=0):
            return mid
        elif arr[mid]==0 and (mid+1 <= len(arr)-1 or arr[mid+1]==0):
            lo=mid+1
        else:
            hi=mid-1
    return mid


print(returnLast0index(arr))

