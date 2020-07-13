arr=[1,3,7,8,9,4,2,1,6]
target=6

def sum2elemenstsEqualtoTarget(ip_arr,target):
    if len(ip_arr)<2:
        return "Entered Array is not valid"
    #res=set()
    res={}
    for i in range (len(ip_arr)):
        item =ip_arr[i]
        diff=target-item
        if item in res:
            print(res)

            if diff in ip_arr:
                return (diff,item)

        else:
            res[diff]=[item]

def sum2elemenstsEqualtoTargetUsingSet(ip_arr,target):
    if len(ip_arr)<2:
        return "Entered Array is not valid"
    res=set()
    #res={}
    for item in ip_arr:
        diff=target-item
        if item in res:
            print(res)
            #if diff in ip_arr:
            return (diff,item)
        else:
            res.add(diff)
def indexOfSum2elemenstsEqualtoTarget(ip_arr,target):
    if len(ip_arr)<2:
        return "Entered Array is not valid"
    #res=set()
    res={}
    for i in range (len(ip_arr)):
        item =ip_arr[i]
        diff=target-item
        if item in res:
            print(res)

            #if diff in ip_arr:
            #return (diff,item)
            return res.get(item)[1],i
        else:
            res[diff]=[item,i]

print(sum2elemenstsEqualtoTarget(arr,target))
print(sum2elemenstsEqualtoTargetUsingSet(arr,target))
print(indexOfSum2elemenstsEqualtoTarget(arr,target))

