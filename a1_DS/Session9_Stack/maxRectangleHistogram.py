'''
https://leetcode.com/problems/largest-rectangle-in-histogram/
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.
Example:
Input: [2,1,5,6,2,3]
Output: 10
'''

def maxRectangle(arr): # approach from notes, needs initialization of stack=[-1]
    if arr==None:
        return "Invalid Array"
    stack=[-1]
    ans=0
    for i in range(0,len(arr)):
        print("-------------------------------------")
        if not stack or arr[stack[-1]]<=arr[i]:
            print("stack: ",stack)
            print("i & arr[i]: ",i,arr[i])
            print("stack[-1] & arr[stack[-1]]: ", stack[-1], arr[stack[-1]])
            stack.append(i)
            print("stack: ",stack)
        else:
            while stack and arr[stack[-1]]>arr[i]:
                print("i & arr[i]: ", i, arr[i])
                print("stack[-1] & arr[stack[-1]]: ", stack[-1], arr[stack[-1]])
                height=arr[stack.pop()]
                print("height: ",height)
                if stack:
                    print("stack[-1]",stack[-1])
                    width=i-stack[-1]-1
                    print("width: ",width)
                    print("height*width: ",height*width)
                    ans=max(ans,height*width)
                    print("ans: ",ans)
            stack.append(i)
        print("stack: ", stack)
        print("i & arr[i]: ", i, arr[i])
        print("stack[-1] & arr[stack[-1]]: ", stack[-1], arr[stack[-1]])
        stack.append(i)
        print("stack: ", stack)
    return ans

#arr=[2,1,5,6,2,3]
#print(maxRectangle(arr))


def maxrect(arr):
    if arr==None:
        return "Invalid array"
    stack=[-1]
    res=0
    arr.append(0)
    for i in range(0,len(arr)):
        while stack and arr[stack[-1]]>arr[i]: # this condition breaks increasing monotonic stack; which means max rectangle can be formed with elements in stack
            max_height=arr[stack.pop()]
            if stack:
                max_width=i-stack[-1]-1
                res=max(res,max_height*max_width)
        stack.append(i) # if not stack or arr[stack[-1]]<=arr[i]:
    return res

arr=[2,1,5,6,2,3]
print(maxrect(arr))

arr=[1]
print(maxrect(arr))

arr=[1,1]
print(maxrect(arr))


