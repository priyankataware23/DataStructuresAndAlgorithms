# Given a pivot element move all elements smaller than pivot to left, and higher to right

#approach : Run 2 for loops.
#           initialize index i=0, and increment as elements are added res[]
#           a. First For loop check all elements that are <=pivot, if yes add to res -- this loop identifies all elements smaller or equal
#           b. In Seconf DOr Loop check all elements greater than pivot, if greater add to res. -- this loop identifies all greater elements

ip_arr=[1,3,4,2,19,20,8,9,23,14,13,-1,19]
pivot=9
expected_op=[1,3,4,2,8,-1,9,19,20,23,14,13,19]

res=[]
i=0
for item in range(0,len(ip_arr)):
    if ip_arr[item]<=pivot:
        res.append(ip_arr[item])
        i+=1

for item1 in range(0,len(ip_arr)):
    if ip_arr[item1]>pivot:
        res.append(ip_arr[item1])
        i+=1
print("input_arr: ", ip_arr)
print("output_arr", res)

# TimeComplexity: 1st for loop - O(n)
#               : 2nd for loop - O(n)
#               : Total - O(n) + O(n) = O(2n) -- O(n)