#find max sum of k elements usisng  consecutive elements of arr

#-3,-3,4 --> 4
# -3,4,-5 -->-4
# 4,-5,6 --> 5
# -5,6,-1 --> 0
# 6,-1,7 -->12
# -1,7,-1 -->5

arr=[3,-3,4,-5,6,-1,7,-1]
k=3

#-- complexity of below is o(nk)

def slidingwindow(arr,k):
    res = []
    sum1 = sum(arr[:k])
    res.append(sum1)
    sum1 = 0
    for i in range(1, len(arr) - k + 1):
        print("----------")
        for j in range(i, i + k):
            print("i & arr[i] ", i, arr[i])
            print("j  arr[j] : ", j, arr[j])
            sum1 += arr[j]
            print(sum1)
        res.append(sum1)
        sum1 = 0
    print(res)
    print("mim:", min(res))
    print("max:", max(res))


print(slidingwindow(arr,k))

def slidingwindow2(arr,k):
    if arr==None or k==None:
        return "Invalid Array"
    max_sum=sum(arr[0:k])
    for i in range(1,len(arr)-k+1):
        max_sum=max(max_sum,sum(arr[i:i+k]))
    return max_sum
print(slidingwindow2(arr,k))



