'''
https://leetcode.com/problems/search-insert-position/
'''


def binarySearchInsertElement(arr, target):
    if len(arr) == 0:
        print("Entered Array is empty")
        return -1
    lo = 0
    hi = len(arr) - 1

    while (lo <= hi):
        mid = lo + (hi-lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    if arr[mid] > target:
        return mid + 1
    else:
        return mid

arr = [10, 11, 13, 15, 19, 23, 34, 35, 40,56]
target = 20
print(binarySearchInsertElement(arr, target))
