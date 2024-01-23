#include<stdio.h>
int main()
{
    int a;
    int b;
    printf("\n Enter the value of A : ");
    scanf("%d",&a);
    printf("\n Enter the value of B : ");
    scanf("%d",&b);
    printf("\n Values before swaping \n a=%d,b=%d ",a,b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("\n Values after swaping \n a=%d,b=%d ",a,b);
    return 0;

}