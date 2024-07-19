# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

def my_sort(lis):
      for i in range(len(lis)):
            temp=lis[i]
            j=i-1
            while (j>=0 and lis[j] > temp):
                  lis[j+1]=lis[j]
                  j-=1
            lis[j+1]=temp


n=int(input("enter a number:"))

lis=[]

for i in range(n):
    ele=int(input("enter a element:"))
    lis+=[ele,]

my_sort(lis)

output=[]

for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        for k in range(j+1,len(lis)):
            if (lis[i]+lis[j]+lis[k]==0 and i!=j!=k):
                output+=[[lis[i],lis[j],lis[k],]]
newlis=[]
       
for i in output:
     if (i not in newlis):
          newlis+=[i,]

print(newlis)
     