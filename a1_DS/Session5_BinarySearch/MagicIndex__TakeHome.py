'''Q2
Magic Index: if in an array, array[i] equals i, then i is called the magic index. Given a sorted array of integers,
find a magic index in the array. There is no duplicates in array.

for eg: arr= [-1,1,12,23,44,55]
 output: 1


 arr= [-2,-1,0,3,44,55]
 output: 3


 arr=[10,102,30,33,40,50]

 output=-1


    '''

def returnMagicIndex(arr):
    if len(arr)==None:
        return -1
    lo=0
    hi=len(arr)-1
    while(lo<=hi):
        mid=lo +(hi-lo)/2
        if arr[mid]==mid:
            return mid
        elif arr[mid]>mid:
            hi=mid-1
        else:
            lo=mid+1
    return -1
arr= [-2,-1,0,3,44,55]
arr1 = [10, 11, 30, 33, 40, 50]

print(returnMagicIndex(arr))
