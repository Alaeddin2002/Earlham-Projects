// Ihsan Alaeddin
// October 13,2021 

#include <stdio.h>

int  max_subarray (int list[],int size) {
// Subarray function
  int max_sum = 0;
  int current_sum = 0;

  int max_start = 0;
  int max_end = 0;
    
  int current_start = 0;
  int current_end = 0;

  for(int i=0; i<size; i++) {
    current_sum = current_sum + list[i];
    current_end = i;
    
    if (current_sum < 0) {
      // if the sum is decreases to below zero we set it to 0 again, and move to the next value
      current_sum = 0;
      current_start = current_end + 1;
    }

    if(max_sum < current_sum)
      // if the current sum is more than the max_sum we have a new max sum and a new max array.\
    {
      max_sum = current_sum;
      max_start = current_start;
      max_end = current_end;
    }
  }
  printf("Maximum SubArray is: %i\n", max_sum);
  printf("Start index of max_Sum: %i\n", max_start);
  printf("End index of max_Sum: %i\n", max_end);
}

int main() {
// Stock Market Function
    int list[] = {-1,2,4,-4,5};
    int size = sizeof(list) / sizeof(list[0]);
    
    max_subarray(list,size);
    
    return 0;
}