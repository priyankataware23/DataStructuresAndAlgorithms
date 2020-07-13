#https://leetcode.com/problems/move-zeroes/
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
ip_arr=[0,1,0,3,1,2,0,3,7,8,0,0,4,0,0,0,0,0]

def movezeros(ip_arr):
    if len(ip_arr)==0:
        return ("Empty Array")
    if len(ip_arr)==1:
        return ip_arr
    zero_ct=0
    for i in range(len(ip_arr)):
        if ip_arr[i]!=0:
            temp=ip_arr[i]
            ip_arr[i]=ip_arr[i-zero_ct]
            ip_arr[i-zero_ct]=temp
        else:
            zero_ct+=1
    return ip_arr

def moveZeros2pointerapproach(ip_arr):
    if len(ip_arr)==1:
        return ip_arr
    i=0
    j=len(ip_arr)-1

    while(i<=j):
        if ip_arr[i]!=0 and ip_arr[j]==0:

            ip_arr[i],ip_arr[j]=ip_arr[j],ip_arr[i]

            i+=1
            j-=1
        elif ip_arr[i]==0:
            i+=1
        else:
            j-=1
    return ip_arr

ip_arr1=[0,1,0,3,1,2,0,3,7,8,0,0,4,0,0,0,0,0]
ip_arr2=[0,0,0,0,0,0,0]
ip_arr3=[0]
ip_arr4=[]
print("=========***********============")
print("input: ",ip_arr1)
print("output: ",movezeros(ip_arr1))
print("=========***********============")

print("input: ",ip_arr2)
print("output: ",movezeros(ip_arr2))
print("=========***********============")

print("input: ",ip_arr3)
print("output: ",movezeros(ip_arr3))
print("=========***********============")
print("input: ",ip_arr4)
print("output: ",movezeros(ip_arr4))

print("======== USING TWO POINTER APPROACH ============== ")

ip_arr5=[0,1,0,3,1,2,0,3,7,8,0,0,4,0,0,0,0,0]
ip_arr6=[0,0,0,0,0,0,0]
ip_arr7=[0]
ip_arr8=[]


print("input: ",ip_arr5)
print("output: ",moveZeros2pointerapproach(ip_arr5))