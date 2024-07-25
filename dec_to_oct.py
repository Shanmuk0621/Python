def dec_to_oct(n):
    s=""
    while (n>0): 
        x=n%8
        s=str(x)+s
        n//=8
    
    print(s)

n=int(input("enter a decimal number"))

dec_to_oct(n)

