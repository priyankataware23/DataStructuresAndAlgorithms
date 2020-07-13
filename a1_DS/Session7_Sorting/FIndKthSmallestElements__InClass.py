# TimeComplexity
# For partition Function

# quickSelect function: Has binary search -- it is calling partition function, rest all steps in this method have constant--O(1) time complexity
# For partition Function
#         -- worst case navigates through all N elements
# -- 1st round goes through N elements
# -- 2ND round goes through n/2
# --3rd round goes through n/3
# O(N +N/2 +N/4 +N/8 + .....) = 2*N --> O(N) -- THIS IS AVG/GOOD CASE TIME COMPLEXITY

# O(N +(N-1) +(N-2) +(N-3)) = N^2 --O(N^2) -- THIS IS WORST CASE TIME COMPLEXITY, WHEN PIVOT FALLS TOWARDS END OF THE ARRAY


def quickSelectRecursion(arr, lo, hi, k):
    while lo <= hi:
        pivot_index = partition(arr, lo, hi)
        print("lo: ", lo)
        print("hi: ", hi)
        if pivot_index == k - 1:
            print("lo: ", lo)
            return arr[pivot_index]
        elif pivot_index > k - 1:
            return quickSelectRecursion(arr, lo, pivot_index - 1, k)
        else:
            return quickSelectRecursion(arr, pivot_index + 1, hi, k)


def quickSelect(arr, k):
    lo, hi = 0, len(arr) - 1
    while (lo <= hi):
        pivot = partition(arr, lo, hi)
        if pivot == k - 1:
            return arr[pivot]
        elif pivot > k - 1:
            hi = pivot - 1
        else:
            lo = pivot + 1


def partition(arr, start, end):
    if arr == None:
        return -1
    pivot = arr[start]
    print("partition function : pivot: ", pivot)
    i = start + 1
    j = end
    while (i <= j):
        if arr[i] > pivot and arr[j] < pivot:
            # print("arr[i]: " , arr[i])
            arr[i], arr[j] = arr[j], arr[i]
        elif arr[i] < pivot:
            i += 1
        else:
            j -= 1
    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    return i - 1  # last element in small group


arr = [13, 2, 3, 3, 1, 6, 11, 1, 4, 5, 6]
print(quickSelectRecursion(arr, 0, len(arr) - 1, 7))
print(arr)

print("============")
arr1 = [13, 2, 3, 3, 1, 6, 11, 1, 4, 5, 6]
print(quickSelect(arr1, 3))

arr3 = [1, 1, 2, 3, 3, 4, 5, 6, 6, 11, 13]
