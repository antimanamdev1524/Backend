#include<iostream>
using namespace std;

main()
{
	int n=6, i, j;
//1
	for(i=0; i<n; i++)
	  {
	    for(j=1; j<=i; j++)
	       {
	       	  printf("%d", i);	       
		   }
		     	printf("\n");
      }
      
          printf("\n\n\n");
//2
    for(i=1; i<n; i++)
      {
      	for(j=1; j<=n-i; j++)
      	  {
      	     printf("%d", i);	
		  }
		     printf("\n");
	  }
//3	  
	for(i=0; i<=n; i++)
	  {
	  	for(j=1; j<=i; j++)
	  	  {
	  	     printf(" * ");	
		  }
		     printf("\n");
	  }
	 
	 for(i=0; i<=n; i++)
	  {
	  	for(j=1; j<=i; j++)
	  	  {
	  	     printf("* ");	
		  }
		     printf("\n");
	  }
//4	  
	  for(i=0; i<=n; i++)
	  {
	  	for(j=1; j<=i; j++)
	  	  {
	  	     printf("*");	
		  }
		     printf("\n");
	  }
	  
//5	  pyramid
	  for(i=0; i<=n; i++)
	  {
	  	for(j=1; j<i; j++)
	  	  {
	  	     printf(" ");	
		  }
	 
	  for(int k=1; k<2*i-1; k++)
	  	  {
	  	     printf("*"); 
     	  }
      }	
	     printf("\n");  
}
