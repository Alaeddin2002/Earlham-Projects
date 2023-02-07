#include <stdio.h>

int main()
{
    FILE *fptr;
    fptr = fopen("student.txt","w");
    int student_number[] = {1150987,689678,6786,5675,5675,6757};
    int grade[] = {77,85,60,82,60,67,77,85,60,82,60,67};
    int credits[] = {3,4,3,1,3,1,3,4,3,1,3,1};
    //number of pairs = n
    int n = 6;
    int j,i;
    //number of lines = l
    int l = 2;
    
    for (j=0;j<l;j++){
         fprintf(fptr,"%d",student_number[j]);
         fprintf(fptr," ");
        for (i=0;i<n;i++){
           fprintf(fptr,"%d",grade[i]);
           fprintf(fptr," ");
           fprintf(fptr,"%d", credits[i]);
           fprintf(fptr," ");
           fprintf(fptr," ");
        }
        fprintf(fptr,"\n");
    }
    
    fprintf(fptr,"%d", -1);
    fclose(fptr);
    return 0;
}
