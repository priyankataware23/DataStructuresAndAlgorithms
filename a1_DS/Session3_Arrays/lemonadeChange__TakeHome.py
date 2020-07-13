'''
At a lemonade stand, each lemonade costs $5.

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.



Example 1:

Input: [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: [5,5,10]
Output: true
Example 3:

Input: [10,10]
Output: false
Example 4:

Input: [5,5,10,10,20]
Output: false
Explanation:
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.

    counter = {5: 0, 10: 0, 20: 0}
    for bill in arr:
        counter[bill] += 1
        if bill == 10:
            if counter[5] > 0:
                counter[5] -= 1
            else:
                return False
        elif bill == 20:
            if counter[10] > 0 and counter[5] > 0:
                counter[10] -= 1
                counter[5] -= 1
            elif counter[5] >= 3:
                counter[5] -= 3
            else:
                return False
    return True

'''


def lemonadestandretchange(arr):
    if len(arr) == 0:
        return False
    if arr[0] != 5:
        return False
    on_hand = {5: 0, 10: 0, 20: 0}
    print(on_hand)

    for bills in range(0, len(arr)):
        if arr[bills] == 5:
            on_hand[5] += 1

        if arr[bills] == 10:
            if on_hand[5] <= 0:
                return False
            elif on_hand[5] >= 1:
                on_hand[5] -= 1
                on_hand[10] += 1

        if arr[bills] == 20:
            if on_hand[5] <= 2 and on_hand[10] == 0:
                return False
            elif on_hand[5] >= 3 and on_hand[10] == 0:
                on_hand[5] -= 3
                on_hand[20] += 1
            elif on_hand[5] <= 2 and on_hand[10] == 1:
                on_hand[5] -= 1
                on_hand[10] -= 1
                on_hand[20] += 1
    print(on_hand)
    return True


arr1 = [5, 5, 5, 10, 20]

print(lemonadestandretchange(arr1))
