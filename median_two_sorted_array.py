

def my_sort(lis):
    for i in range(n+m):
        temp=lis[i]
        j=i-1
        while (j>=0 and lis[j] > temp):
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=temp


def median(lis):
    if ((n+m)%2==0):
        print("the median is : ",(lis[(n+m)//2]+lis[((n+m)//2)-1])/2)
    else:
        print("the median is : ",lis[n//2])



n=int(input("enter a no of elements in list1"))

lis1=[]

for i in range(n):
    ele=int(input("enter a element"))
    lis1+=[ele,]

m=int(input("enter a no of elements in list2"))

lis2=[]

for i in range(m):
    ele=int(input("enter a element"))
    lis2+=[ele,]

merge_lis=[]
merge_lis=lis1

for i in range(m):
    merge_lis+=[lis2[i]]

print(merge_lis)
    
my_sort(merge_lis)

print(merge_lis)
median(merge_lis)