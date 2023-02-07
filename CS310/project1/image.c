/** 	CS310 Project 1
File: imagesstack.c
Name: IHSAN ALAEDDIN
Date: October 17,2021
*/  

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[]){
    FILE* fp = fopen(argv[1], "r");
    FILE* negative = fopen(argv[2], "wb");
    FILE* flip = fopen(argv[3], "wb");
    int i,j, maxVal, width, height;
    
    char fileType[3];
    
    if (fp == NULL){
        printf("Error opening\n");
        exit(EXIT_FAILURE);
    }
    
    fscanf(fp, "%s%d%d%d", fileType, &width, &height, &maxVal);
    fprintf(negative, "%s\n%d %d\n%d\n", fileType, width, height, maxVal);
    fprintf(flip, "%s\n%d %d\n%d\n", fileType, width, height, maxVal);
    int numberArray[height][width];
    int rotated[height][width];
    
    for(i=0;i< height ; i++){
        for(j=0;j<width;j++){
            fscanf(fp, "%d", &numberArray[i][j]);
         }
       }
    
    for(i = 0; i < height; i++) {
        for(j = 0; j < width; j++){
            fprintf(negative, "%d ", (maxVal - numberArray[i][j]));
        }
             fprintf(negative, "\n");
    }
    
     for(i = 0; i < height; i++) {
        for(j = 0; j < width; j++){
        rotated[i][j] = numberArray[height-j-1][i];}}
      
    
    for(i=0;i< height ; i++){
        for(j=0;j<width;j++){
            fprintf(flip,"%d ",rotated[i][j]);
        }
        fprintf(flip,"\n");
    }
    fclose(fp);
    fclose(negative);
    fclose(flip);
}



