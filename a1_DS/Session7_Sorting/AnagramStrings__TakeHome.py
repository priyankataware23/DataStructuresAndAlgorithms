'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Time Complexity:  O(N) + O(N) + O(N) == O(3N) --> O(N)
'''
str1 = "anagzram"
str2 = "nazagram"
map1 = dict()
map2 = dict()
for c in str1:
    if c in map1:
        map1[c] += 1
    else:
        map1[c] = 1



def check_anagram(s, t):
    if s == None or t == None: # Time complexity: O(1)
        return -1
    if len(s) != len(t): # Time complexity: O(1)
        return False

    map1 = dict()
    map2 = dict()

    for c in s: # Time complexity: O(n)
        if c in map1:
            map1[c] += 1
        else:
            map1[c] = 1

    for c in t: # Time complexity: O(n)
        if c in map2: # Time complexity: O(1)
            map2[c] += 1 # Time complexity: O(1)
        else:
            map2[c] = 1 # Time complexity: O(1)
    print(map1)
    print(map2)

    for item in map1: # Time complexity: O(N)
        if item not in map2: # Time complexity: O(1)
            return False
        if map1[item]!=map2[item]: # Time complexity: O(1)
            return False
    return True


print(check_anagram(str1, str2))
