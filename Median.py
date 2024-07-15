# Median of the data

n=int(input("enter the no of elements"))

lis=[]

for i in range(n):
    ele=int(input("enter a element"))
    lis+=[ele,]

for i in range(n):
    temp=lis[i]
    j=i-1
    while (j>=0 and lis[j] > temp):
        lis[j+1]=lis[j]
        j-=1
    lis[j+1]=temp

print(lis)

if (n%2==0):
    print("the median is : ",(lis[n//2]+lis[(n//2)-1])/2)
else:
    print("the median is : ",lis[n//2])