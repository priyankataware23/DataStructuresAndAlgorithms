from collections import  OrderedDict
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

def firstUniqChar(s):
    if len(s) == 0:
        return -1
    res = OrderedDict()
    print(s)
    s = "".join([c if c.isalpha() else "" for c in s]).lower()
    print(s)
    for c in s:
        if c in res:
            res[c] = res[c] + 1
        else:
            res[c] = 1

    item = -1
    for i in range(0, len(s)):
        if res[s[i]] == 1:
            item = i
            break
    return max(-1, item)

str1="aabbccddeeffg"
print(firstUniqChar(str1))

