'''
QS FInd missing number is a sequence

1. Given an array startitng from 0, has a sequence of numbers.
Find the 1st missing number in the array. Array can have more than 1 number missing. No duplicates in array

For eg : arr=[0,1,2,3,4,5,7,8,9,11]  ; expected op = 6 ;

Follow up qs:
2. Given an array starting from non-zero number, has a sequence of numbers.
Find the 1st missing number in the array. Array can have more than 1 number missing. No duplicates in array

For eg : arr=[100,101,102,103,104,105,107,108,109,111]  ; expected op = 106 ;


Follow up qs:
3. Given an array starting from 0, has a sequence of numbers.
Find the kth missing number in the array. Array can have more than 1 number missing. No duplicates in array


For eg : arr=[0,1,2,3,4,5,6,7,11] ; k=2; expected op = 9 ;


--=========
1. This can be solved with 2 pointer approach, that will be linear complexity O(n)
2. Or can also be solved with Binary Search technique, complexity will be O(log N)

'''

# Solution for qs 1.

print("==========================")
def missingNumberSeqStartingFromZero(arr):
    if arr==None:
        return -1
    lo,hi=0,len(arr)-1
    while(lo<=hi):
        mid=int(lo+ (hi-lo)/2)
        if arr[mid]==mid and (mid+1<len(arr) and arr[mid+1]-arr[mid]>1):
            return arr[mid]+1
        elif arr[mid]==mid:
            lo=mid+1
        else:
            hi=mid-1
    return -1

arr=[0,1,2,3, 4,5,6,8,9,10,11,13]
print (missingNumberSeqStartingFromZero(arr))

print("==========================")
# Solution for qs 2.
def missingNumberSeqStartingNonZero(arr):
    if arr==None:
        return -1
    lo,hi=0,len(arr)-1
    while(lo<=hi):
        mid=int(lo+(hi-lo)/2)
        if arr[mid]==mid+arr[0] and mid+1<len(arr) and arr[mid+1]-arr[mid]>1:
            return arr[mid]+1
        elif arr[mid]==mid+arr[0]:
            lo=mid+1
        else:
            hi=mid-1
    return -1

arr1=[100,101,102,103,104,105,107,108,109,111]

print(missingNumberSeqStartingNonZero(arr1))

print("==========================")
# Solution for qs 3.

def findKthmissingNumberSeq (arr,k):
    if arr==None or k<=0:
        return -1
    lo,hi=0,len(arr)-1
    while(lo<=hi):
        mid=int(lo+(hi-lo)/2)
        if arr[mid]<mid+k and mid+1<len(arr) and arr[mid+1]>mid+1+k:
            ct_missing_elem_before_mid=arr[mid]-mid
            return arr[mid] + (k-ct_missing_elem_before_mid)


def missingElement(arr, k):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        # at most k - 1 missing element before arr[mid] and at least k elements missing before arr[mid+1]
        if arr[mid] < mid + k and mid + 1 < len(arr) and arr[mid + 1] >= mid + 1 + k:
            # how many element are missing before mid?
            missing_elements_before_mid = arr[mid] - mid

            return arr[mid] + (k - missing_elements_before_mid)


        elif arr[mid] < mid + k:  # left side of mid has nothing missing
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


print("==========================")
arr2=[0,1,2,3,4,6,7,8,10,16,17]
print (missingElement(arr2,2))
