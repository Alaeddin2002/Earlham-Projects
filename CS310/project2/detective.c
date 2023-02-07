/** 	CS310 Project 1
File: imagesstack.c
Name: IHSAN ALAEDDIN
Date: October 26,2021
*/  

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include <time.h>
#include "mysterysorts.h"

// category 0 is O(n log(n)), 1 is O(n^2)
int time_category(int sort) {

  //TODO
  
  return 0;
}

/* Must return an exact name for one of the possible algorithms:
 * bubble sort 
 * insertion sort 
 * selection sort 
 * heap sort
 * merge sort
 * quicksort
 *
 * Can return UNKNOWN if algorithm could not be determined.
 */
char* classify(int sort) {

  //TODO
  
  return "UNKNOWN";
}

int main(){
    double elapse;
        int i,j, n = 18, algorithm = 0;
    int test[] = {-100,-300,-3,2,89,6,39,76,202,19,38,48,36,29,-7,1,99,500};
    int lst2[n],lst4[n]; 
    int max=0,loc = 0,min = 0, huge,random,random2,random3,second,sec;
    
    
    
    // Calculate time
    for (i=0;i<n;i++){
       lst4[i] = test[i]; }
    struct timeval start, finish;
    gettimeofday(&start, 0);
   mysterySort(test,n,algorithm,-1);

  gettimeofday(&finish, 0);
  elapse = (finish.tv_sec - start.tv_sec)*1000000
	+ finish.tv_usec - start.tv_usec;

    // calculate Minimum Number
    for (i=0;i<n;i++){
        if (test[i]<test[min]){
            min = i;}
       
    }
  // calculate Maximum Number
    for (i=0;i<n;i++){
        if (test[i]>test[max]){
            huge = i;}
    }
    // If Array begins with the minimum number, place it last to see how an algortithm performs
    if (test[0] == test[min]){
       random = test[0];
        test [0] = test[n-1];
        test [n-1] = random;
    }
     // If Array ends with the maximum number, place it third to see how an algortithm performs
    if (test[n-1] == test[huge]){
       random3 = test[n-1];
        test [n-1] = test[2];
        test [2] = random3;
    }
    // calculate second to minimum Number and place it first to see how an algorithm performs
    if (test[0] < test[1]) {
        min =test[0];
        second = test[1];
    }
    else {
      min = test[1];
      second = test[0];
    }
    for (i = 2; i < n; i++) {
        if (test[i] < min) {
        second = min;
        min = test[i];
        }
        else if (test[i] < second) {
            second = test[i];
        }
    }
    
    for (i=0;i<n;i++){
        if (test[i] == second){
            sec = i; }}
    
    if (test[0] != second){
        random2 = test[0];
        test [0] = test[sec];
        test [sec] = random2;
    }
    
    

    for (i=0;i<n;i++){
         lst2[i] = test[i];}
    
    mysterySort(test,n,algorithm,0);
    

    for (i=0;i<n;i++){
        if (lst2[i]<lst2[loc]){
            loc = i;}
    }
        
    for (i=0;i<n;i++){
        if (lst2[i]>lst2[max]){
            max = i;}
    }
    ////////////////////////////////////////////////////////////////////////
  // if algorithm changes the array from step 0
    for (i=0;i<n;i++){
    if (lst2[i] != test[i]){
        if (lst2[loc] == test[0]){
             // if algorithm places the minimum first from step 0
            if (lst2[1] == test[1]){
                // Quick sort changes two elements in step 0, so element in space 1 would be the same.
                printf(" the list is a Selection Sort with time complexity of O(n^2) of time %f\n",elapse);
                return 0;} 
             // Insertion sort places max at the end of array in step 0 and minimum at the start.
            else if (lst2[max] == test[n-1]){
                printf(" the list is a Bubble Sort with time complexity of O(n^2) of time %f\n",elapse);
                return 0;} 
            else if(round((n/5)-5) <= elapse && elapse <=round((n/5)+5)){
                printf(" the list is a Quick Sort with time complexity of O(n^2) of time %f\n",elapse);
                return 0;} 

        }
        // Insertion sort may place max at the end of array in step 0 and second to last at the start.
        else if (lst2[max] == test[n-1] && second == test[0]){
                printf(" the list is a Bubble Sort with time complexity of O(n^2)of time %f\n",elapse);
                            return 0;} 

            else{
            printf(" the list is a Heap Sort with time complexity of O(nlogn) of time %f\n",elapse);
                                return 0;} 

    return 0 ;}
    
        
    }
    
    mysterySort(test,n,algorithm,3);
     
  for (i=0;i<n;i++){
      for (j=i+1;j<n;j++){
          if (lst2[i] == lst4[j]){
              if ((round(n-2)/3) == elapse){
                  printf("the list is a Merge Sort with time complexity of O(nlogn) of time %f\n",elapse);
                                  return 0;} 

              if (n>20){
                if ((round((n-2)/3)-5) <= elapse && elapse <=(round((n-2)/3)+5)){
               // Heap sort swaps two elements next to each other so i in step 0 would equal i+1 in step 3.
              printf("the list is a Merge Sort with time complexity of O(nlogn) of time %f\n",elapse);
                          return 0;} 
              }
                  else if ((round((n-2)/3)-1) <= elapse && elapse <=(round((n-2)/3)+1)){
               // Heap sort swaps two elements next to each other so i in step 0 would equal i+1 in step 3.
              printf("the list is a Merge Sort with time complexity of O(nlogn) of time %f\n",elapse);
                return 0;} 
          }
      }
  }
    // if none of the criteria is atisfied the algorithm is a Heap sort
          printf("the list is an Insertion Sort with time complexity of O(n^2) of time %f\n",elapse);
                return 0;

   ///////////////////////////////////////////////////////////////////////// 
  

     
}



