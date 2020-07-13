'''
Given a/b return int portion of quotient

for eg: 7/2 should return 3
14/3 should return 4
16/4 should return 4


'''

def divide2Nos(a,b):
    if a==None or b==None:
        return -1
    if b==0:
        return 0
    hi=a
    lo=0
    ans=0
    while(lo<=hi):
        mid=int(lo +(hi-lo)/2)
        if mid*b==a:
            ans=mid
            return ans
        elif mid*b<a:
            lo=mid
            ans=mid
        else:
            hi=mid
    return ans

print (divide2Nos(18,18))


