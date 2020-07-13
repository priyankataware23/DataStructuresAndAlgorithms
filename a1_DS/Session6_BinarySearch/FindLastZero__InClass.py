'''
Below solution is using binary search
'''

def findlastzero(arr):
    if len(arr) == 0:
        return -1
    lo, hi = 0, len(arr) - 1

    while (lo <= hi):
        mid = lo + (hi - lo) / 2
        print("mid: ",mid)
        if arr[mid] == 0 and (mid== len(arr)-1 or arr[mid + 1] == 1):
            return mid
        elif arr[mid+1] == 0 :
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


arr = [0,0,0,0,0,0,0]
arr1=[1,1,1,1,1,1]
arr2=[0,0,0,0,1,1,1]
arr3=[0,1,1,1]
arr = [0,0,0,0,0,1,1]

print(findlastzero(arr))
