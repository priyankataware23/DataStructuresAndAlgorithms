'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

'''


##below solution exceeds runtime expectations on leetcode
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = int(lo + (hi - lo) / 2)
        if nums[mid] == target:
            return True
        if nums[lo] == nums[mid]:  # Fail to estimate which side is sorted
            lo += 1  # In worst case: O(n)
        elif nums[lo] < nums[mid]:  # Left side of mid is sorted
            if nums[lo] <= target <= nums[mid]:  # Target in the left side
                hi = mid - 1
            else:  # in right side
                lo = mid + 1
        else:  # Right side is sorted
            if nums[mid] <= target <= nums[hi]:  # Target in the right side
                hi = mid - 1
            else:  # in left side
                lo = mid + 1
    return False


def returnSearchElementSortedArrWithDups(arr, target):
    if arr == None:
        return False
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) / 2

        if arr[mid] == target:
            print("Target Found at index: ", mid)
            return True
        if mid + 1 < len(arr) and arr[lo] < arr[mid]:
            if arr[lo] <= target <=arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        elif mid + 1 < len(arr) and arr[lo] > arr[mid]:
            if arr[mid] <= target <= arr[hi]:
                lo = mid - 1
            else:
                hi = mid + 1
        else:
            if arr[lo] == arr[mid]:
                lo += 1
            if arr[hi] == arr[mid]:
                hi -= 1
        return False


arr = [2, 5, 6, 0, 0, 1, 2]
target = 2
print(search(arr, target))

print("=========")
arr1 = [6, 6, 7, 0, 1, 2, 3]
target = 2
print(search(arr1, target))

print("=========")
arr3 = [2, 5, 6, -1,0, 1, 2]
target = 2
print(returnSearchElementSortedArrWithDups(arr3, target))

print("=========")
arr4 = [4, 5, 6, 7, 0, 2, 3, 4]
target = 2
print(returnSearchElementSortedArrWithDups(arr4, target))
