'''
https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Approach: using stack, and push index to it.

1. traverse through array
2. at each index, check while stack  & arr[i]>arr[stack[-1]] --{approach here is to keep on adding indices to stack, until we find a element which is greater that recently added element to stack}
        top=stack.pop() --[this forms a container to hold water]

        if stack:
            dist_btn_2_tow= i - stack-1 -1
            eq_height_btn_2_tow = min(arr[i],stack[-1]) - arr[top] --{height of container}
            res+=dist_btn_2_tow*eq_height_btn_2_tow
3. append most recent index to stack
4. return res


'''



def trapRainWater(arr):
    if arr==None:
        return "Invalid Array"
    stack=[]
    res=0
    for i in range(0,len(arr)):
        while stack and arr[i]>arr[stack[-1]]:
            top=stack.pop()
            if stack:
                dist_btn_tow=i-stack[-1]-1
                eq_ht_btn_two=min(arr[i],arr[stack[-1]])-arr[top]
                res+=(dist_btn_tow*eq_ht_btn_two)
        stack.append(i)
    return res

Input=[1,0,2,1,0,1,3,2,1,2,1]
print(trapRainWater(Input))
