#include<iostream>
using namespace std;
main()
{
	int i, j, k;
	for(i=0; i<=5; i++) //row
	 {
	 	for(j=i; j<=5; j++)
	 	 {
	 	    printf("*");
		 }
	   printf("\n");		   
	 }
	 
	 printf("----------\n\n");
	
	for(i=0; i<=5; i++)
	 {
	 	for(j=i; j<=5; j++)
	 	 {
	 	 	printf("\n");
		  }
		  printf(" *");
		  
	 }
}
