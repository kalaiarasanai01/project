#include <iostream>
using namespace std;

/*class firstsource
{
public :
        float a,b,c;
        int multiplication();
        int division();


        int addition()
{
        cout<<"\n---Addition Program---";
        cout<< "\nEnter the Value of A:";
        cin>>a;
        cout<< "Enter the Value of B:";
        cin>>b;
        c=a+b;

        cout<<"\nThe Added Value of " <<a <<" + " <<b<< " is:"<<c<<"\n";
}
        int subtraction()
{
        cout<<"\n---Subtraction Program---";
        cout<< "\n Enter the Value of A:";
        cin>>a;
        cout<< " Enter the Value of B:";
        cin>>b;
        c=a-b;
        cout<<"\nThe Subtracted Value of " <<a <<" - " <<b<< " is:"<<c<<"\n";
}
};*/

class mercury
{
public:
    void dell()

    {
        int age;
    if (age>=18,age<=50)
    {
        cout <<"you are eligible for working";
    }
    else
    {
        cout <<"you are not eligible age not matching";
    }

}
void dell(string name)
    {
        int age;
    if (age>=18,age<=50)
    {
        cout <<"you are eligible for working";
    }
    else
    {
        cout <<"you are not eligible age not matching";
    }
    }

};


/*int firstsource :: division()
{
    float a, b, c;
        cout<<"\n---Division Program---";
        cout<< "\nEnter the Value of A:";
        cin>>a;
        cout<< "Enter the Value of B:";
        cin>>b;
        c=a/b;
        cout<<"\n The divided Value of " <<a <<" / " <<b<< " is:"<<c<<"\n";
}
int mercury :: multiplication(int a,int b)
{
c=a*b;
cout<<"\n Multiplication value of " <<a<<" * " << b<<  " is:"<<c<<"\n";
}
int mercury :: */

int main()
{
 //firstsource Ak,fs;
//Ak.addition();
//fs.subtraction();
//Ak.multiplication();
//fs.division();
mercury my;
int age;
cout << "enter your age";
cin >>age;
string name;
cout <<"enter your name";
cin >>name;
//my.addition();
my.dell();

    return 0;
}
