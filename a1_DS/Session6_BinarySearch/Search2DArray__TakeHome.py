'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

# this code on submission exceeded execution time
def search2darray(mat,target):
    if mat==None:
        return False
    for i in mat:
        if i[0]<=target<=i[len(i)-1]:
            lo=0
            hi=len(i)-1
            while(lo<=hi):
                mid=int(lo+(hi-lo)/2)
                if i[mid]==target:
                    return True
                elif i[mid]<target:
                    lo=mid+1
                else:
                    hi=mid-1
        elif i[len(i)-1]<target:
            continue
    return False

mat = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print(search2darray(mat,target))

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target1 = 13

print(search2darray(matrix,target1))

matrix2 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target2 = 30

print(search2darray(matrix2,target2))


def searchTwoDMatrix(matrix,target):
    if matrix==None or target==None or len(matrix)==0 or len(matrix[0])==0:
        return False
    row=len(matrix)
    col=len(matrix[0])
    lo=0
    hi=(row*col)-1
    while lo<=hi:
        mid=int(lo+(hi-lo)/2)
        r,c = divmod(mid,col)
        print("r: ",r ,"c: ",c)
        if matrix[r][c]==target:
            return True
        elif matrix[r][c]<target:
            lo=mid+1
        else:
            hi=mid-1
    return False

print(searchTwoDMatrix(matrix2,30))

