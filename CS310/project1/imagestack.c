/** 	CS310 Project 1
File: imagesstack.c
Name: IHSAN ALAEDDIN
Date: October 17,2021
*/  

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>



int main(int argc, char *argv[]){
    int i,j,k,m, maxVal, width, height,temp;
    FILE* fp[argc-2];
    FILE* outputFile = fopen(argv[argc-1], "w");

    char fileType[3];
    
    for(i = 1; i < argc-1; i++) {
        
        fp[i-1] = fopen(argv[i], "r");
        if (fp[i-1] == NULL){
        printf("Error opening\n");
        exit(EXIT_FAILURE);
        }
        fscanf(fp[i-1], "%s%d%d%d", fileType, &width, &height, &maxVal);
    }
    
    int*** numberArray = (int***) malloc(sizeof(int **)*argc-2);
    for(k=0; k < argc-2; k++){
        numberArray[k] = (int**)malloc( sizeof(int*)*height);
    }
    for(j=0; j<argc-2; j++){
        for(m=0; m<height; m++){
            numberArray[j][m] = (int *)malloc( sizeof(int)*width);
        }
    }

    int *twoDArray[height];
    for (j = 0; j < height; j++)
        twoDArray[j] = (int*)malloc(width * sizeof(int));
 
    int count = 0;
    for (j = 0; j < height; j++)
        for (k = 0; k < width; k++)
            twoDArray[j][k] = ++count; 

        
        

    for(m = 0; m < argc-2; m++) {    
        for(j=0;j< height ; j++){
            for(k=0;k<width;k++){
                fscanf(fp[m], "%d", &numberArray[m][j][k]);
          }
       }
    }
   
    fprintf(outputFile, "%s\n", fileType); 
    fprintf(outputFile, "%d ", width);
    fprintf(outputFile, "%d\n", height);
    fprintf(outputFile, "%d\n", maxVal);  
    
     for(j=0;j< height ; j++){
            for(k=0;k<width;k++){
                twoDArray[j][k] = 0; }}
    
    
    
      for(m = 0; m < argc-2;m++) {    
          for(j=0;j< height ; j++){
            for(k=0;k<width;k++){
                twoDArray[j][k] = twoDArray[j][k] + numberArray[m][j][k];   
           }
        }
     }
    
        
    for(j=0;j< height ; j++){
            for(k=0;k<width;k++){
                fprintf(outputFile, "%d\n", twoDArray[j][k]/(argc-2));
            }
    }
    fclose(*fp);
    fclose(outputFile);
}