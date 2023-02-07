#include <stdio.h>

int main()
{

    int ID_Number = 1150987;
    
    FILE *fptr;
    fptr = fopen("student.txt","r");
    int num,num2=0;
    //number of pairs = n
    int n = 6;
    int i,j;
    //number of lines = l
    int l = 2;
    int ID[l];
    int num3[l];
    
   for (j=0;j<l;j++){
        
        for (i=0;i<((n*2)+1);i++){

            fscanf(fptr,"%d", &num);
            if (num<=100){
                if (i%2!=0){
                    num2 += num;}
            }
             else{
                 ID[j] = num;}
        }
       num3[j] = num2/n;
       num2=0;
   }
      
    for (j=0;j<l;j++){
        if (ID_Number == ID[j]){
        printf("%d",ID[j]);
        printf(" ");
        printf("accumulative average is ");
        printf("%d",num3[j]);
        printf("\n");
        }
    }
            
    


       fclose(fptr); 
  
       return 0;
}


