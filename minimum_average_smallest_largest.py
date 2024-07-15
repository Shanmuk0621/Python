# 3194. Minimum Average of Smallest and Largest Elements

# You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

# You repeat the following procedure n / 2 times:

# Remove the smallest element, minElement, and the largest element maxElement, from nums.
# Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.

def my_min(lis):
    min=lis[0]
    for i in range(len(lis)):
        if ( min > lis[i]):
            min=lis[i]
    return min


def my_max(lis):
    max=lis[0]
    for i in range(len(lis)):
        if ( max < lis[i]):
            max=lis[i]
    return max

def my_remove(lis,ele):
    newlis=[]
    count=0
    for i in range(len(lis)):
        if (ele==lis[i]):
            break
        else:
            count+=1
            newlis+=[lis[i],]
    
    for i in range(count+1,len(lis)):
        newlis+=[lis[i],]
    return newlis
    

n=int(input("enter a no of element"))

lis=[]

for i in range(n):
    ele=int(input("enter a element"))
    lis+=[ele,]

output=[]

k=int(n/2)

for i in range(k):
    min=my_min(lis)
    max=my_max(lis)
    avg=(min+max)/2
    output+=[avg]
    temp=my_remove(lis,min)
    print(temp)
    temp1=my_remove(temp,max)
    lis=temp1
    print(lis)

print(output)
print(my_min(output))
