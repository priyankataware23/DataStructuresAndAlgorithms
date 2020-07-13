'''

https://leetcode.com/problems/exclusive-time-of-functions/


On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.



Example 1:
image:
https://assets.leetcode.com/uploads/2019/04/05/diag1b.png

Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.


Note:

1 <= n <= 100
Two functions won't start or end at the same time.
Functions will always log when they exit.

'''

def exclusiveTimeOfFunc(arr,n):
    if arr==None or n<=0:
        return "Invalid Array"
    id_stack=[]
    prev_start_time=0
    res=[0 for i in range (0,n)]
    i=0
    while (i<len(arr)):
        item=arr[i]
        val=item.split(":")
        id=int(val[0])
        event=val[1]
        time=int(val[2])
        if event=='start':
            if id_stack:
                res[id_stack[-1]]+= time - prev_start_time
            id_stack.append(id)
            prev_start_time=time
        else:
            if id_stack and id_stack[-1]==id:
                res[id_stack[-1]]+=time-prev_start_time+1
                id_stack.pop()
                prev_start_time=time+1
        i+=1
    return res



n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

print(exclusiveTimeOfFunc(logs,n))
