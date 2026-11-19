#include<iostream>
using namespace std;

class bank
{
	public:
		char name[20];
		string account_num;
		int balance= 5000, deposite, withdrawl;
		
		details()
		{
		   cout<<"Enter name: ";
		   cin>>name;
	   
		   do
	     {
	     	cout<<"account_number: ";
		    cin>>account_num;
		   if(account_num.length()==12)
		   cout<<"Current Balance: "<<balance;
		   else
		   cout<<"\nplease Enter 12 digits of your account correctly.. \n";
	     } 
	     
		   while(account_num.length()!=12);		   
		}
		   
		choose()
		 {
		 	int choice;
		    cout<<"\n\nPress_1 for deposit \n Press_2 for withdraw\n: ";
		    cin>>choice;
		    
		    switch(choice)
		    {
		    	case 1:
		    		deposit();
		    	break;
		    	case 2:
		    		withdraw();
		    	break;
			}
		 }
	
		deposit()
		{
			cout<<"\n\ndeposit amount: ";
			cin>>deposite;
			
			if (deposite==0)
			cout<<"Total balance: "<<balance;
			else
			cout<<"Total balance: "<<balance+deposite;
		}
		
		withdraw()
		{
			cout<<"\n\nwithdraw amount: ";
			cin>>withdrawl;
		  if(balance>=withdrawl)
		   {
			if(deposite==0)
			cout<<"current balance: "<<balance - withdrawl;
			else
			cout<<"after withdrawl \n your current account balance is: "<<balance + deposite - withdrawl;
	       }
	      else
	       {
	       	  cout<<"Amount is not sufficient!!"
		   }
		}		
};

main()
{
	bank obj;
	obj.details();
	obj.choose();
//	obj.deposit();
//	obj.withdraw();
}
