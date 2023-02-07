// Ihsan Alaeddin
// October 7,2021 

#include <stdio.h>

/* IN C, a function must specify 
   what type of data it returns. 
   This function returns a int */

int main()
{
    int x;
    char name[20];
    int i = 12;
    
    printf("hello World\n");
    
    for (int i = 0; i < 3; i++){
        printf("Welcome!\n");
        printf("Hi!\n");
    }
    
    printf ("Please enter your name.\n");
    scanf("%s",name);
    printf("please enter your time.\n");
    scanf("%d",&x);
    
    printf("%l\n", &i);      
    return 0;
}