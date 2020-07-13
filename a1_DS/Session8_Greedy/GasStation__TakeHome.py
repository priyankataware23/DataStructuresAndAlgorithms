'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input:
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Solution:
consider gas [] as total gas you can fill in your tank at every stop. & to travel to next gas - stop you need to travel
-- cost (consider as distance in miles. With an assumption 1 mile= 1 gallon of gas )
so ideally to travel to next gas stop you need to have more gas as compared to distance to be covered

keep track of extra gas & lessby gas at each stop, at the end of for loop if extra + lessby >=0 then round trip can be made.

Good youtube video: https://www.youtube.com/watch?v=nTKdYm_5-ZY&t=213s

'''

def gasStation (gas,cost):
    if gas == None or cost ==None:
        return "Invalid parameters passed to function"
    extra,lessby,start=0,0,0
    for i in range(0,len(gas)):
        extra=extra + gas[i] -cost[i]
        if extra<0:
            lessby= lessby + extra
            extra=0
            start=i+1
    return start if extra+lessby>=0 else -1

gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
print("sample1 ----")
print(gasStation(gas,cost))

gas1=[1,2,3,4,3,2,4,1,5,3,2,4]
cost1=[1,1,1,3,2,4,3,6,7,4,3,1]
print("sample2 ----")
print(gasStation(gas1,cost1))



