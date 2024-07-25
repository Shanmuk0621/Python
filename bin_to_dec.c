#include <stdio.h>
#include <math.h>

int mypow(int x,int y)
 {
    int p=1;
    for(int i=1;y>=i;i++)
    {
        p*=x;
    }
    return p;
 }
int main()
{
    int a,x=0,power,d,sum;
    printf("enter a bin num:");
    scanf("%d",&a);
    while(a>0)
    {
     d=a%10;
    //  power=mypow(2,x);
     power=pow(2,x);
     sum+=d*power;
     x++;
     a=a/10;

    }
    printf("decimal number : %d",sum);
    return 0;
}