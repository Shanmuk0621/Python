# Mode of the number set

n=int(input("enter a number of elements:"))

lis=[]

for i in range(n):
    ele=int(input("enter a element:"))
    lis+=[ele,]

undplicate=[]

for i in lis:
    if i not in undplicate:
        undplicate+=[i,]

print(undplicate)

count_lis=[]

for i in range(len(undplicate)):
    count=0
    for j in range(n):
        if ( undplicate[i] == lis[j]):
            count+=1
    count_lis+=[count]

print(count_lis)

max=count_lis[0]
j=0
for i in range(len(count_lis)):

    if (max < count_lis[i]):
        max=count_lis[i]
        j=i

print(undplicate[j])


