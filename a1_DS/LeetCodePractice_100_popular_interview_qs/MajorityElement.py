'''
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''




def majorityElement(nums):
    if nums == None:
        return "Empty array passed"
    hsmp = dict()
    for val in nums:
        if val in hsmp:
            hsmp[val] = hsmp.get(val) + 1
        else:
            hsmp[val] = 1
    for item in hsmp:
        if hsmp[item] > len(nums) / 2:
            return item
    return -1

arr=[2,2,1,1,1,2,2]
arr1=[3,2,3]
print(majorityElement(arr))
print(majorityElement(arr1))