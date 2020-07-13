'''

https://leetcode.com/problems/asteroid-collision/
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input:
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input:
asteroids = [8, -8]
Output: []
Explanation:
The 8 and -8 collide exploding each other.
Example 3:
Input:
asteroids = [10, 2, -5]
Output: [10]
Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input:
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation:
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
'''
def asteriodcollision(arr):
    if arr==None:
        return "Invalid Array"
    stack=[]
    for item in arr:
        #append all positive numbers to stack
        if item>0:
            stack.append(item)
        else:
            #we get 1st opposite side element, for which we need to pop elements from stack if winning direction is -ve, else don't add -ve items to stack
            while stack and stack[-1]>0 and stack[-1] + item <0:
                stack.pop()
            if not stack or stack[-1]<0: # if stack has all -ve numbers or stack is empty then append -ve numbers
                stack.append(item)
            elif stack[-1]+item==0:
                stack.pop()
    return stack


# discussed in class -- ask for solution
def asteriods(arr):
    if arr==None:
        return "Invalid array"
    i=0
    stack=[]
    res=[]
    while(i<len(arr)):
        if arr[i]>0:
            if stack and stack[-1]>arr[i]:
                stack.append(arr[i])
                i+=1

        else:
            if stack and abs(stack[-1])>abs(arr[i]):
                i+=1
            elif stack and abs(stack[-1])<=abs(arr[i]):
                stack.pop()
                print(stack)
            elif not stack:
                res.append(arr[i])
                print(res)
        res.append(stack)
    return res

arr=[15,10,-5,-5,5,-20,5]
print(asteriodcollision(arr))

