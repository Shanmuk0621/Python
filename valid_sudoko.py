# 36. Valid Sudoku
# Medium
# Topics
# Companies
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.




n=int(input("enter a number of dimensions:"))

lis=[]
for i in range(n):
    a=[]
    for j in range(n):
        ele=(input("enter a element"))
        a+=[ele,]
    lis+=[a,]

rc=0
for i in range(n):
    cc=0
    k=i
    for j in range(n-1):
        if(lis[i][j]==lis[i][j+1]): 
            cc+=1
        if (lis[j][i]==lis[j+1][i]):
            cc+=1

    if (cc!=0):
        # print(cc)
        print("false")
        break

count=0
for i in range(1,n+1,i=3*i):
    for j in range(1,n+1,j=j*3):
        for k in range(1,n+1):
            print()





for i in range(n):
    for j in range(n):
        print(lis[i][j],end=" ")
    print("\n")


# print(lis)
