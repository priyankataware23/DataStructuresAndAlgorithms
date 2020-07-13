'''
Qs. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4


'''

def firstSingleNumber_UsingSet(nums):
    if nums == None:
        return ("Entered Array is empty")
    dups=set()
    for val in nums:
        if val not in dups:
            dups.add(val)
        else:
            dups.remove(val)
        #print(dups)
    return dups.pop()


def firstSingleNumber_UsingHashMap(nums):
    if nums==None:
        return "Entered Array is empty"
    hash_mp=dict()
    for val in nums:
        if val in hash_mp:
            hash_mp[val]= hash_mp.get(val)+ 1
        else:
            hash_mp[val] = 1
    for item in hash_mp:
        if hash_mp[item]==1:
            return item




arr=[2,2,1]
print(firstSingleNumber_UsingSet(arr))
print ("***")
print(firstSingleNumber_UsingHashMap(arr))

print ("------------")
arr1=[4,1,2,1,2,5]
print(firstSingleNumber_UsingSet(arr1))
print ("***")
print(firstSingleNumber_UsingHashMap(arr1))


