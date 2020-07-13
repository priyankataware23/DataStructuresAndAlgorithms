'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity [O(n)].
 Could you implement it using only constant extra space complexity? O(1)
'''



def findMissingNumber(ip_arr):
    if len(ip_arr)==0:
        print("Entered Array is empty")
    if len(ip_arr)==1:
        return ip_arr
    arr_sum=sum(ip_arr)
    n=len(ip_arr)
    res= (n*(n+1)/2 ) -arr_sum # sum=3+0+1=4 ; n=3 ; n*n(n+1)/2 ;(3*4/2==6); 6-4 ; 2

    return res
ip_arr=[]
ip_arr1=[1]
ip_arr2=[0,1,2,3,4,5,6,7,8,9,11]
print("Empty Array: ",findMissingNumber(ip_arr))
print("Array with length==1 : ",findMissingNumber(ip_arr1))
print("Valid Array: ",findMissingNumber(ip_arr2))

