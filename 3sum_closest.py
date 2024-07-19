
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0)



def my_sort(lis):
      for i in range(len(lis)):
            temp=lis[i]
            j=i-1
            while (j>=0 and lis[j] > temp):
                  lis[j+1]=lis[j]
                  j-=1
            lis[j+1]=temp

def my_min(lis):
     min=lis[0]
     for i in range(len(lis)):
          if(min > lis[i]):
               min=lis[i]
     return min

n=int(input("enter a no of elements:"))

lis=[]

for i in range(n):
    ele=int(input("enter a element:"))
    lis+=[ele,]

target=int(input("enter a target element:"))

sumlis=[]
for i in range(n-2):
        sumlis+=[lis[i]+lis[i+1]+lis[i+2]]


my_sort(sumlis)


difflis=[]
for i in range(len(sumlis)):
    if (sumlis[i] < target):
        difflis+=[target-sumlis[i],] 
    else:
        difflis+=[sumlis[i]-target] 
    


min=my_min(difflis)


for i in range(len(sumlis)):
    if (sumlis[i] < target):
        just=target-sumlis[i]
    else:
        just=sumlis[i]-target

    if (just==min):
         print(sumlis[i])
         break 

        



