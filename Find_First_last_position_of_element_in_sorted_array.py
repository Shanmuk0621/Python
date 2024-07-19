# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

def my_sort(lis):
    for i in range(len(lis)):
        temp=lis[i]
        j=i-1
        while ( j>=0 and lis[j]>temp):
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=temp



n=int(input("enter a no of element"))

lis=[]
for i in range(n):
    ele=int(input("enter a element"))
    lis+=[ele,]

target=int(input("enter a target element"))

my_sort(lis)

for i in lis:
    print(i,end=" ")

print("\n")
c=0
for i in range(n):
    if (lis[i]==target and c==0):
        print(i)
        c+=1
    if (lis[i] == target and lis[i+1]!=target):
        print(i)
        


