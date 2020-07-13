arr = [1,2,2,3,3]


def returnNonDuplicate(arr):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]
    lo = 0;
    hi = len(arr) - 1
    print("arr length: ",len(arr))

    while (lo <= hi):
        print("==========")
        print("lo: ", lo)
        print("hi: ", hi)

        mid = lo + (hi - lo) / 2
        print("mid: ", mid)

        #l_odd = (mid - low) % 2 == 1
        #l_even = not l_odd
        #r_odd = (high - mid) % 2 == 1
       # r_even = not r_odd

        l_odd =  (mid - lo) % 2 == 1
        print("l_odd: ", l_odd)

        l_even = not l_odd
        print("l_even: ", l_even)

        r_odd =  hi - mid % 2 == 1
        print("r_odd: ", r_odd)

        r_even = not r_odd
        print("r_even: ", r_even)


        if lo == mid == hi:
            return arr[mid]
        if l_even == 1 and arr[mid - 1] == arr[mid]:
            hi = mid - 2
        elif r_even == 1 and arr[mid + 1] == arr[mid]:
            lo = mid + 2
        elif l_odd == 1 and arr[mid - 1] == arr[mid]:
            lo = mid + 1
        elif r_odd == 1 and arr[mid+1] == arr[mid]:
            hi = mid - 1
    return None

print(returnNonDuplicate(arr))