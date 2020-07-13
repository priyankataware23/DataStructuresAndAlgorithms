# In class session.

# Given a String, find count of words in string. Count in words--
# i.e. any special characters - ' or , or " or . empty spaces should not be considered as word

# approach:
# Clean string - a. get rid of all non alpha numeric characters, and convert all words to lower.
#                b. convert string to array, by splitting it by a space
#                c. Create a dict in which key will be word, and value will be count of occurrence
#                d. Return dict

# Time complexity is O(n) -- iterate over string and convert it to array-- for loop
#                    O(n) -- iterate over array of words
#                    O(n) -- Insert Elements to dict
# Total Time complexity : O(n)+O(n)+O(n)= O(3n) equivalent to 0(n)

ip_str="Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food"
print("input string: " + ip_str)
clean_str="".join([i if i.isalpha() else " " for i in ip_str]).lower() # this gets rid of all characters other than alphabets, join converts array to string and convers string to lower

print("clean string: "+ clean_str)

arr=clean_str.split(" ")
print(arr)

res=dict()

for item in arr:
    if item: # this will return true only when item is not empty . this takes care of empty spaces
        if item in res:
            res[item]+=1
        else:
            res[item]=1

print(res)
