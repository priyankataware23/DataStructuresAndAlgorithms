'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def returnThreeSum(arr,trg):
    if len(arr)==0:
        return -1
    res=set()
    arr.sort()
    print(arr)
    for c in range(0,len(arr)-1):
        lo=0
        hi=len(arr)-1
        while  (c >lo and c <hi):
            if arr[c]+arr[lo]+arr[hi]==trg:
                res.add((arr[c],arr[lo],arr[hi]))
                lo+=1
                hi-=1
            elif arr[c]+arr[lo]+arr[hi]>trg:
                hi-=1
            else:
                lo+=1
    return res

nums = [-1, 0, 1, 2, -1, -4]
print(returnThreeSum(nums,0))



