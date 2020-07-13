'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Solution
Create 2 variable curr_sum ; max_sum have then to hold val= arr[0]


'''

def maxSumSubarray(arr):
    if arr==None:
        return "Invalid Array passed as parameter"
    curr_sum=arr[0]
    max_sum=arr[0]
    for val in arr[1:]:
        curr_sum= max(curr_sum+val,val)
        if max_sum<curr_sum:
            max_sum=curr_sum
    return max_sum

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSumSubarray(arr))