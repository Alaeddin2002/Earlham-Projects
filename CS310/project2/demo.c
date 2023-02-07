/* 
 * This is a sample driver that tests the performace of mysterySort algorithm 0
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include "mysterysorts.h"

int main(){
  int sort = 5;
  int maxSteps = 100;
  int n = 200;
  int a[n];
  //random seed helps ensure same numbers across runs
  srand ( 42 ); // change to time(0) if you want purely random

  for( int i = 0; i < n; i++ ){ 
	a[i] = rand()%1000;
  }

  //run sort without interruption
  struct timeval start, finish;
  double elapse;
  gettimeofday(&start, 0);
  
  mysterySort(a, n, sort, -1);

  gettimeofday(&finish, 0);
  elapse = (finish.tv_sec - start.tv_sec)*1000000
	+ finish.tv_usec - start.tv_usec;
  printf("Time to fully sort %d items: %f microseconds\n\n", n, elapse);

  //create new unsorted data
  //random seed helps ensure same numbers across runs
  srand ( 42 );
  printf("original:\n");
  for( int i = 0; i < n; i++ ){
	a[i] = rand()%1000;
	printf("%d ", a[i]);
  }
  printf("\n\n");
 
  //interrupt sort after a given number of steps
  mysterySort(a, n, sort, maxSteps);
  
  //check current array content
  printf("current:\n");
  for( int i = 0; i < n; i++ ){ 
	printf("%d ", a[i]);
  }
  printf("\n");
}
