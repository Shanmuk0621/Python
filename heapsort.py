def heapify(lis,n,i):
    large=i
    left=2*i+1
    right=2*i+2

    if ( left <n and lis[left] > lis[large]):
        large=left
    if ( right < n and lis[right] > lis[large]):
        large=right

    if (large != i):
        # temp=lis[i]
        # lis[i]=lis[large]
        # lis[large]=temp
        lis[i],lis[large]=lis[large],lis[i]
        heapify(lis,n,large)

def heap_sort(lis,n):
    for i in range(int((n/2)-1),-1,-1):
        heapify(lis,n,i)
    
    for i in range(n-1,-1,-1):
        # temp=lis[i]
        # lis[i]=lis[0]
        # lis[0]=temp
        lis[i],lis[0]=lis[0],lis[i]
        heapify(lis,i,0)

n=int(input("enter no of elements"))

lis=[]

for i in range(n):
    ele=int(input("Enter a element"))
    lis+=[ele,]


print(lis)

heap_sort(lis,n)

for i in range(n):
    print(lis[i])

