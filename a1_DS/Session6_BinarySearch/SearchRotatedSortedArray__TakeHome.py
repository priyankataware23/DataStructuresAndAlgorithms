'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''

def searchElement(arr,t):
    if len(arr)==0:
        return -1
    lo,hi=0,len(arr)-1
    while(lo<=hi):
        print("========================")
        print("lo: ",lo)
        print("hi: ",hi)
        print("t: ",t)
        mid=lo+(hi-lo)/2
        print("mid: ",mid)
        if arr[mid]==t:
            return mid
        elif (arr[mid]>arr[mid-1])and (mid + 1 < len(arr) and arr[mid] >arr[mid + 1]):
            if arr[mid]<t:
                hi=mid
            else:
                lo=mid
        elif (arr[mid]>arr[mid-1])and (mid + 1 < len(arr) and arr[mid] < arr[mid + 1]):
            if arr[mid]<t:
                hi=mid
            else:
                lo=mid
    return -1


def returnSearchElementSortedArr(arr,t):
    if arr==None:
        return -1
    lo,hi=0,len(arr)-1
    while(lo<=hi):
        print("====================")
        print("lo: ",lo)
        print("hi: ",hi)
        mid=int(lo+(hi-lo)/2)
        print("mid: ",mid)
        print("t: ",t)
        if arr[mid]==t:
            return mid
        if arr[lo]<arr[mid]: # elements of left of mid are sorted
            print("arr[lo]: ",arr[lo])
            print("arr[mid]: ", arr[mid])
            if arr[lo]<=t<=arr[mid]: # checks if target lies between lo & mid
                hi=mid-1
                print("hi: ",hi)
            else: # since target not between lo & mid increment lo=mid+1
                lo=mid+1
                print("lo: ", lo)
        else: # elements of left are not sorted
            if arr[mid]<=target<=arr[hi]: # checks if target between mid & hi
                hi=mid-1
            else: # since target not between hi & mid increment lo=mid+1
                lo=mid+1
    return -1




nums = [4,5,6,7,0,1,2,-1,-4,-8,-9]
target = -8
print(returnSearchElementSortedArr(nums,target))
