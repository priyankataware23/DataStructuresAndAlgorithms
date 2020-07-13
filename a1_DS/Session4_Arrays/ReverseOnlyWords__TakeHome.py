'''

https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string, reverse the string word by word.



Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
'''


def reverseOnlyWords(s):
    if s == None:
        return "Empty String"
    arr = s.split()
    i = 0
    j = len(arr) - 1
    while (i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    s = " ".join(arr)
    return s


s = "hello world, hello java       world, hello python world"
print("input string: " + s)
print ("output string: "+ reverseOnlyWords(s))
