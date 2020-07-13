def maxProduct(arr):
    curr_prod=arr[0]
    max_prod=arr[0]
    for val in arr[1:]:
        curr_prod=max(curr_prod*val,val)
        if max_prod<curr_prod:
            max_prod=curr_prod
    return max_prod

arr=[-2,3,-4]
print(maxProduct(arr))