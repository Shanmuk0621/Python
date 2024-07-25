

def dec_to_bin(n):
    s=""
    while (n>0):
        x=n%2
        s=str(x)+s
        n//=2
    print(s)



n=int(input("enter a number"))


dec_to_bin(n)