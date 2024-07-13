# Pascal's Triangle


n=int(input("enter a number of rows"))

for i in range(n):
    i_fact=1
    t=i
    print((n-i) * " ",end=" ")
    while(t>0):
        i_fact*=t
        t=t-1
    for j in range(i+1):
        j_fact=1
        T=j
        while(T>0):
            j_fact*=T
            T=T-1

        i_j_fact=1
        x=i-j

        while(x>0):
            i_j_fact*=x
            x=x-1
        
        print(int( (i_fact) / (i_j_fact*j_fact) ),end=" ")
    print(" ")

        


