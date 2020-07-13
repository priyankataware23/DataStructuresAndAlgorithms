#https://leetcode.com/problems/monotonic-array/
'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
'''

def checkMonoTone(ip_arr):
    if ip_arr==None:
        return ("Empty Array")
    flg="UNKNOWN" # FLag can have values as "UNKNOWN" ,'GROWING', 'DROPPING . By default we will set it to UNKNOWN
    for i in range(0,len(ip_arr)):
        print("index: ", i ,"Value: ",ip_arr[i])

        if ip_arr[i]<=ip_arr[i+1]:
            if flg=="UNKNOWN":
                flg="GROWING"
                print (flg)
            if flg!="UNKNOWN" and flg=="GROWING":
                flg = "GROWING"
            if flg!="UNKNOWN" and flg!="GROWING":
                return("Array is not Monotone")

        if ip_arr[i]>=ip_arr[i+1]:

            if flg=="UNKNOWN":
                flg="DROPPING"
                print("first_pass: ", flg)

            if flg!="UNKNOWN" and flg=="DROPPING":
                flg = "DROPPING"
                print("Further Passes at index: " ,i,"Value of flag: ",flg)
            if flg<>"UNKNOWN" and flg<>"DROPPING":
                return("Array is not Monotone")

        else:
            return ("Array is Monotone")
    return flg

ip_arr=[6,5,4,4]
ip_arr1=[1,2,2,3]
ip_arr2=[1,3,2]

print(checkMonoTone(ip_arr))



## Practice

def monotone_Arr(arr):
    if len(arr)==0:
        print("Entered Array is empty")
        return "Empty Array"
    if len(arr)==1:
        return ("Array is monotone")
    flg="unkown" # Can have values as unknown; growing; dropping

    for i in range(0,len(arr)-1):
        if arr[i]<=arr[i+1]:
            if flg=="unkown":
                flg="growing"
            if flg !="unknown" and flg=="growing":
                flg=="growing"
            if flg!="unkown" and flg!="growing":
                return ("Entered Array is not monotone")


        if arr[i]>=arr[i+1]:
            if flg=="unknown":
                flg="dropping"
            if flg != "unknown" and flg == "dropping":
                    flg="dropping"
            if flg !="unknown" and flg!="dropping":
                return ("Entered Array id not monotone")

        #else:
         #   return ("Array is Monotone")

        return flg

ip_arr=[6,5,4,4]
ip_arr1=[1,2,2,3]
ip_arr2=[2,2,2]
print("=====")
print(monotone_Arr(ip_arr2))