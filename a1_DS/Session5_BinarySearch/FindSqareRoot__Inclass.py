'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

Below method is binary search method

Complexity: O(log n)
'''


def returnSqrt(x):
    if x == 0:
        return x
    if x == 1 or x == -1:
        return x
    lo = 1
    hi = int(x / 2)
    print("start hi: ", hi)
    print("start lo: ", lo)
    ans = 0

    while (lo <= hi):
        print("In while hi: ", hi)
        print("In while lo: ", lo)
        mid = int(lo + (hi - lo) / 2)
        print ("In while mid: ", mid)

        if mid * mid == x:
            print("In if mid: ", mid)
            ans = mid
            print("In if ans: ", ans)
            return ans
        elif mid * mid < x:
            print("elif mid: ", mid)
            lo = mid + 1
            ans = mid
            print("elif ans: ", ans)
        else:
            hi = mid - 1
            print("else hi: ", hi)
            print("else lo: ", lo)
            print ("ans :", ans)
    return ans


num = 50
print(returnSqrt(num))

def returnsqrt(x):
    if x == 0 or x == 1:
        return x
    lo = 1
    hi = int(x / 2)
    ans = 0
    while (lo <= hi):
        mid = int(lo + (hi - lo) / 2)
        if mid * mid == x:
            ans = mid
            return ans
        elif mid * mid < x:
            lo = mid + 1
            ans = mid
        else:
            hi = mid - 1
    return ans
num = 50
print ("==========")
print(returnsqrt(num))


#-- Practice

def findSqrt(num):
    if num==0 or num==1 or num ==-1:
        return num
    lo=1
    hi=int(num/2)
    ans=0
    while(lo<=hi):
        mid=lo+(hi-lo)//2
        if mid *mid==num:
            ans=mid
            return mid
        elif mid*mid < num:
            lo=mid+1
            ans=mid
        else:
            hi=mid-1
    return ans

print(findSqrt(7))

def exactSqrt(num):
    if num==0 or num==1 or num==-1:
        return num
    lo=0
    hi=int(num/2)
    ans=0
    for i in range(0,10000):
        mid=float(lo+(hi-lo)/2)
        if mid*mid==num:
            ans=mid
            return ans
        elif mid*mid < num:
            lo=mid+1
            ans=mid
        else:
            hi=mid-1
    return ans

print(exactSqrt(13))

