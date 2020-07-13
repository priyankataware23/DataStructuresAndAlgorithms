# https://leetcode.com/problems/valid-palindrome/
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Time Complexity: O(n)
'''

def isvalidpalindrome(ip_str):
    if ip_str == None:
        print("Entered String is empty")

    # Cleansing string , get rid of all spaces, special characters anything other than alphabets & digits. & convert string to lower
    ip_str="".join([c if c.isalnum() else "" for c in ip_str]).lower()
    #print(ip_str)
    if len(ip_str)==1:
        return True

    start = 0
    end = len(ip_str)-1

    while start<end:
        if ip_str[start]==ip_str[end]:
            start += 1
            end -= 1
        else:
            return False

    return True




str1 = "A man, a plan, a canal: Panama"
str2="race a car"
print("========")
print("input: ",str1 ," result: " , isvalidpalindrome(str1))
print("========")
print("input: ",str2 ," result: " , isvalidpalindrome(str2))


