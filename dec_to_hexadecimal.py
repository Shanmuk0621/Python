
def dec_to_hexa(n):
    s=""

    while(n>0):
        x=n%16
        if (x==10):
            s='A'+s
        elif (x==11):
            s='B'+s
        elif (x==12):
            s="C"+s
        elif (x==13):
            s='D'+s
        elif (x==14):
            s="E"+s
        elif (x==15):
            s="F"+s
        else:
            s=str(x)+s
        n//=16

    print(s)



n=int(input("enter a decimal number:"))

dec_to_hexa(n)
