# 33. Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

def my_sort(lis):
    for i in range(len(lis)):
        temp=lis[i]
        j=i-1
        while (j>=0 and temp < lis[j] ):
            a[j+1]=a[j]
            j-=1
        
n=int(input("enter a no of element"))

lis=[]

for i in range(n):
    ele=int(input("enter a element"))
    lis+=[ele,]

k=int(input("enter a target element"))


my_sort(lis)

newlis=[]

for i in range(k,n):
    newlis+=[lis[i]]

for i  in range(0,k):
    newlis+=[lis[i],]

print(newlis)

c=0

for i in range(n):
    if (k==newlis[i]):
        c+=1
        print("at index of :",i)
        break

if (c==0):
    print("-1")

