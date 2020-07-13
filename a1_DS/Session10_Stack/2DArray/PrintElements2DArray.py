
# print elements row wise from left to right
def printElements2Darr(arr):
    if arr==None:
        return "Invalid Array"
    rows=len(arr)
    col=len(arr[0])

    for i in range(0,rows):
        for j in range (0,col):
            print(arr[i][j], end=" ")
        print()


#print elements row wise right to left

def printElementsRowWise_right_to_left(arr):
    if arr==None:
        return "Invalid Array"
    rows=len(arr)
    cols=len(arr[0])
    for k in range (0,rows):
        i=k
        j=cols-1
        while(j>=0):
            print(arr[i][j],end=" ")
            j-=1
        print()

#print elements row wise:  left to right ; but print in reverse row order ; i.e. print last row 1 st and so on.
def printElementsRowWise_left_to_right_reverese_row(arr):
    if arr==None:
        return "Invalid Array"
    rows=len(arr)
    cols=len(arr[0])
    #Loop through the array in reverse order that is, the loop will start from (rows - 1) and end at 0 [-1] by decreasing (hence -ve) the value of k by 1.
    for k in range (rows-1,-1,-1):
        i=k
        j=0
        while(j<cols):
            print(arr[i][j],end=" ")
            j+=1
        print()




# print elements column wise top to bottom

def printElementsColumn(arr):
    if arr==None:
        return "invalid array"
    rows=len(arr)
    cols=len(arr[0])
    for k in range (0,cols):
        j=k
        i=0
        while(i<rows):
            print(arr[i][j], end=" ")
            i+=1
        print()

# print elements column wise bottom to top

def printElementsColumn_btm_2_top(arr):
    if arr==None:
        return "invalid array"
    rows=len(arr)
    cols=len(arr[0])
    for k in range (0,cols):
        j=k
        i=rows-1
        while(i>=0):
            print(arr[i][j], end=" ")
            i-=1
        print()


## Print Diagonally
def printElements2DarrDiagonally(arr):
    if arr==None:
        return "Invalid Array"
    rows=len(arr)
    cols=len(arr[0])
    for k in range(0,rows):
        i=k
        j=0
        while (i>=0 and j<cols):
            print(arr[i][j],end=" ")
            i-=1
            j+=1
        print()

    for k in range(1,cols):
        i=rows-1
        j=k
        while(i>=0 and j<cols):
            print(arr[i][j], end=" ")
            i-=1
            j+=1
        print()


#print diagonally
def printDiagonaly(arr):
    if arr==None:
        return "Invalid array"
    rows=len(arr)
    cols=len(arr[0])
    for k in range(rows-1,-1,-1):
        i=k
        j=cols-1
        while(i<rows and j>=0):
            print(arr[i][j],end=" ")
            i+=1
            j-=1
        print()
    for k in range(cols-2,-1,-1):
        j=k
        i=0
        while(i<rows and j>=0):
            print(arr[i][j],end=" ")
            i+=1
            j-=1
        print()

''' https://leetcode.com/problems/spiral-matrix/submissions/ '''
def print2DSpiral(arr):
    if len(arr)==0:
        return []
    nos_row=len(arr)
    nos_col=len(arr[0])
    s_row=0
    s_col=0
    res=[]

    while(s_row<nos_row and s_col<nos_col):

        for i in range(s_col,nos_col):
            #print(arr[s_row][i], end=" ")
            res.append(arr[s_row][i])
        s_row+=1


        for i in range(s_row,nos_row):
            #print(arr[i][nos_col-1] ,end=" ")
            res.append(arr[i][nos_col-1])
        nos_col-=1


        if s_row<nos_row:
            for i in range (nos_col-1,s_col-1,-1 ):
                #print(arr[nos_row-1][i],end=" ")
                res.append(arr[nos_row-1][i])
            nos_row-=1

        if s_col<nos_col:
            for i in range(nos_row-1,s_row-1,-1):
                #print(arr[i][s_col],end=" ")
                res.append(arr[i][s_col])
            s_col+=1
    return res












arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
printElements2DarrDiagonally(arr)
print("===========================================")
printElements2Darr(arr)
print("===========================================")
printElementsColumn(arr)
print("===========================================")
printElementsColumn_btm_2_top(arr)
print("===========================================")
printElementsRowWise_right_to_left(arr)
print("===========================================")
printElementsRowWise_left_to_right_reverese_row(arr)
print("===========================================")
printDiagonaly(arr)

print("===========================================")
print(print2DSpiral(arr))