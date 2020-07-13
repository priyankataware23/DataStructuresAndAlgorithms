'''
Creating 2d matrix
'''
# Create a 2d list /matrix
r=2
c=2
mat=[]

for i in range(0,2):
    mat.append([])
print(mat)

for i in range(0,r):
    for j in range(0,c):
        mat[i].append(j)
        mat[i][j]=0

print(mat)
'''
print("========== Create 2D Matrix, by taking input from users ==============")

row=int(input("Enter Nos of rows"))
col=int(input("Enter Nos of cols"))
mat1=[]

for i in range(0,row):
    mat1.append([])
print(mat1)

for i in range(0,row):
    for j in range(0,col):
       mat1[i].append(j)
       print("------")
       print(mat1)
       print("Enter value to be added at position: ", "row: ",i+1,"col: ",j+1)
       mat1[i][j]=int(input())

print(mat1)
'''
mat3=[[10,11,12],[15,16,18],[23,26,29]]
target=26
print(len(mat3))

for i in mat3:
    lo=0
    hi=len(i)-1
    while(lo<=hi):
        mid=lo+(hi-lo)//2
        print("mid: ",mid)
        print("i[mid]: ",i[mid])
        if i[mid]==target:
            print(i[mid])
            break
        if i[mid]<target:
            hi=mid-1
        else:
            lo=mid+1


def searchin2DMatrix(mat,target):
    if mat==None:
        return -1
    for i in mat:
        lo=0
        hi=len(i)
        while (lo<=hi):
            mid=lo+(hi-lo)//2
            if i[mid]==target:
                return i[mid]
            elif i[mid]<target:
                hi=mid-1
            else:
                lo=mid+1
    return -1

print(searchin2DMatrix(mat3,target))

