#include<stdio.h>
int main()
{
    int num;
    printf("Enter any 1 or 2 digit num ");
    scanf("%d",&num);
    if (num<0 || num>=99)
   {
     printf(" Invalid Number ");
   }
    else
    {
        printf("Enter the number");
        switch (num)
        {
            case 0: printf(" ZERO ");
            break;
            case 10: printf(" TEN ");
            break;
            case 11: printf(" ELEVEN ");
            break;
            case 12: printf(" TWELVE ");
            break;
            case 13: printf(" THIRTEEN");
            break;
             case 14: printf("FOURTEEN");
            break;
             case 15: printf("FIFTEEN");
            break;
             case 16: printf("SIXTEEN");
            break;
             case 17: printf("SEVENTEEN");
            break;
             case 18: printf("EIGHTEEN");
            break;
             case 19: printf("NINETEEN");
            break;
            default: switch (num/10)
            {
            case 2: printf("TWENTY");
            break;
             case 3: printf("THIRTY");
            break;
             case 4: printf("FOURTY");
            break;
             case 5: printf("FIFTY");
            break;
             case 6: printf("SIXTY");
            break;
             case 7: printf("SEVENTY");
            break;
             case 8: printf("EIGHTY");
            break;
             case 9: printf("NINTY");
            break;
            }
        }
        switch (num%10)
        {
             case 1: printf("ONE");
            break;
             case 2: printf("TWO");
            break;
             case 3: printf("THREE");
            break;
             case 4: printf("FOUR");
            break;
             case 5: printf("FIVE");
            break;
             case 6: printf("SIX");
            break;
             case 7: printf("SEVEN");
            break;
             case 8: printf("EIGHT");
            break;
             case 9: printf("NINE");
            break;
        }
    }
}        


