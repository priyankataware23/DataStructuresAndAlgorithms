#Write a program that outputs the string representation of numbers from 1 to n.
#if n is multiple of 3 print fizz, if multiple of 5 print buzz, if multiple of both print fizzbuzz
#Example: n = 15,
#op:["1","2","Fizz","4","Buzz","Fizz", "7","8", "Fizz","Buzz", "11","Fizz","13","14","FizzBuzz"]

arr=[]
for i in range(1,16):
    tmp=""
    if i%3==0:
        tmp="Fizz"
    if i%5==0:
        tmp+="Buzz"
    arr.append(tmp if tmp else str(i))


print(arr)
