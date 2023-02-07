#include <stdio.h>

#define max 5

int a[max + 1] = { 5,4,3,2,6,7 };
int b[max];

void merging(int low, int mid, int high) {
   int l1, l2, i;

   for(l1 = low, l2 = mid + 1, i = low; l1 <= mid && l2 <= high; i++) {
      if(a[l1] <= a[l2])
         b[i] = a[l1++];
      else
         b[i] = a[l2++];
   }
   
   while(l1 <= mid)    
      b[i++] = a[l1++];

   while(l2 <= high)   
      b[i++] = a[l2++];

   for(i = low; i <= high; i++)
      a[i] = b[i];
}

void sort(int low, int high) {
   int mid;
   
   if(low < high) {
      mid = (low + high) / 2;
      sort(low, mid);
      sort(mid+1, high);
      merging(low, mid, high);
   } else { 
      return;
   }   
}

int main() { 
   int i;
   int value = 5;
   int j = max - 1;
    
   sort(0, max);

   
   
   
   while(max > i){ 
       if (a[i] + a[j] == value) { 
          printf("%d ", a[i]);
          printf("%d ", a[j]);
          return 1;}
       else if (a[i] + a[j] < value){
           i = i + 1;
   }
       else {
           j = j - 1; }
   }
   return -1;
       
}