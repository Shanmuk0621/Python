# 1637. Widest Vertical Area Between Two Points Containing No Points

# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.

 

# Example 1:

# ​
# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1
# Explanation: Both the red and the blue area are optimal.
# Example 2:

# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3


def mysort(lis):
    for i in range(n):
        temp=lis[i]
        j = i-1
        while (j>=0 and lis[j] < temp):
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=temp


n=int(input("enter the no of cordinates"))
m=int(input("enter the no of coordinates"))

coordinates_lis=[]

for i in range(n):
    a=[]
    for j in range(m):
        ele=int(input("enter the coordinates"))
        a+=[ele,]
    coordinates_lis+=[a,]

print(coordinates_lis)

mysort(coordinates_lis)

# print(coordinates_lis)

temp_lis=[]

for i in range(n):
        if (coordinates_lis[i][1] != 0 and coordinates_lis[i][0] not in temp_lis):
            temp_lis+=[coordinates_lis[i][0]]
            

# print(temp_lis)

print(temp_lis[0] - temp_lis[1])