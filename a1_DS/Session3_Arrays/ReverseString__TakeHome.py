'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
'''

s = "a-bC-dEf-ghIj"



ch = list(s)
print(ch)

start = 0
end = len(s) - 1

while (start <= end):
    if not ch[start].isalnum() and not ch[end].isalnum():
        start+=1
        end-=1
    elif ch[start].isalpha() and not ch[end].isalpha():
        end-=1
    elif not ch[start].isalpha() and ch[end].isalpha():
        start+=1
    else:
        ch[start],ch[end]=ch[end],ch[start]
        start+=1
        end-=1
print(ch)
s1="".join(ch)
print(s1)





def reverseString (s):
    if not s:
        return "empty string"
    arr=list(s)
    print("[")
    print(arr)
    print("]")
    start,end = 0,len(arr)-1
    while (start<=end):
        if arr[start].isalnum() and arr[end].isalnum():
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
        elif not arr[start].isalpha():
            start+=1
        else:
            end-=1

    s="".join(arr)
    return s
print(s)
print("==============")
print(reverseString(s))






