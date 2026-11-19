#include<iostream>
using namespace std;
main()
{
    int a, b;
    cout<<"A: ";
    cin>>a;

    cout<<"B: ";
    cin>>b;

// 10+6=16 a=10, b=6
// 16-6=10  b=10
// 16-10=6  a=6

    a=a+b;    
    b= a-b;
    a= a-b;

    cout<<"A: "<<a;
    cout<<"B: "<<b;
}  
