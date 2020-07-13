'''

https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

def validParenthesis(str):
    if len(str)%2==1: # since we check valid pairs, nos of items in str shd be even
        return False
    stack=[]
    #Keep position of opening & closing parenthesis in sync
    open_item=['(','[','{']
    close_item=[')',']','}']


    for item in str:
        #append only open_item to stack
        if item in open_item:
            stack.append(item)
        elif stack and item in close_item:
            # get the position of item in close_item, and open_item will hv same open parenthesis at same index
            # we don't run while loops here, as we compare 1 item at a time. -- each close can pop only 1 open item
            pos=close_item.index(item)

            if stack[-1]==open_item[pos]:
                stack.pop()
            else:
                return False
        else:
            return False
    return False if stack else True

print("[] : ",validParenthesis("[]"))
print("()[]{}  : ",validParenthesis("()[]{}"))
print("(] : ",validParenthesis("(]"))
print("([)] : ",validParenthesis("([)]"))
print("{[]} : ",validParenthesis("{[]}"))
