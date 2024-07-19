# 35. Search Insert Position
# Easy
# Topics
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output:


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

for i in range(n):
    if (lis[i] == target):
        print(i)
    elif ( lis[i]<target and i<n-1 and target<lis[i+1]):
        print(i+1)
    elif (lis[i]>=lis[n-1] and lis[i]<target):
        print(i+1)

     



