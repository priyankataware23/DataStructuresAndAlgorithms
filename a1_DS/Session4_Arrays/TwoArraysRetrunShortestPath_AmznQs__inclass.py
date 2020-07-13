maxDistance = 10500
forwardShippingRoutes = [2500, 4000, 7500, 10000]
backwardShippingRoutes = [1000, 2500, 3000, 5000, 9000, 11000]

'''return 1 element from forwardShippingRoutes and other from backwardShippingRoutes which sums to maxDistance.
else return -1
'''

i = 0
j = len(backwardShippingRoutes) - 1


def shippingRoutes(maxDistance,forwardShippingRoutes,backwardShippingRoutes):
    i = 0
    j = len(backwardShippingRoutes) - 1
    while (i <= len(forwardShippingRoutes) - 1 and j >= 0):
       # print("fwd:",forwardShippingRoutes[i])
       # print("fwd:", backwardShippingRoutes[j])
        if forwardShippingRoutes[i] + backwardShippingRoutes[j] == maxDistance:
            return (forwardShippingRoutes[i], backwardShippingRoutes[j])
        elif forwardShippingRoutes[i] + backwardShippingRoutes[j] < maxDistance:
            i += 1
        else:
            j -= 1
    return -1
maxDistance = 10500
forwardShippingRoutes  = [2500, 4000, 7500, 10000]
backwardShippingRoutes = [1000, 2500, 3000, 5000, 9000, 11000]
print(shippingRoutes(maxDistance, forwardShippingRoutes,backwardShippingRoutes))