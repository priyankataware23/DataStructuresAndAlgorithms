def reverseWords(s):
    return  " ".join([i for i in s.strip().split(' ')[::-1] if i])
str1="     the sky is blue   "
#print(reverseWords(str1))

def reverseWord(s):
    if not s:
        return "Empty String"
    if len(s)==1:
        return s
    arr= s.strip().split(" ")
    start=0
    end=len(arr)-1
    while (start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    s=(" ").join(arr)

    return s

print(reverseWord(str1))


def reverseCharactersWords(str):
    if not str:
        return "Empty String"
    arr=str.strip().split(" ")
    print (arr)
    for item in arr:
        print (item)
        print(len(item))
        start=0
        end=len(item)-1
        print(start)
        print(end)
        while (start<end):
            print(item[start])
            print(item[end])
            item[start],item[end]=item[end],item[start]
            start+=1
            end-=1
        print(arr)
    str=(" ").join(arr)

    return str

print(reverseCharactersWords(str1))














