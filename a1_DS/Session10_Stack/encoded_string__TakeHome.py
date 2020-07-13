'''
Decode String
aonecode.com
  Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated k times. Note that k is guaranteed to be a positive integer. You may assume that the original data does not contain any digits and that digits are only for those repeat numbers.
e.g.
input
s = "3[a]2[bc]" expected output "aaabcbc"
input
s = "3[a2[c]]xy"
expected output
return "accaccaccxy".

'''

def decodeString(str):
    if str == None:
        return "Invalid String"
    stack = []
    for val in str:
        print("========================")
        if val != ']':
            stack.append(val)
        else:
            item = ''
            while stack:
                print(stack)
                x = stack.pop()
                if x == '[':
                    n=""
                    while stack and stack[-1].isdigit():
                        n = stack.pop() + n
                    stack.append(int(n) * item)
                    print("after: ",stack)
                    break
                else:
                    item = x + item

    return "".join(stack)


print(decodeString("ab3[a]2[bc]"))
#print(decodeString("3[a2[c]]xy"))
#print(decodeString("100[leetcode]"))

