#include<stdio.h>

#define size 4

 int arr1[] = {2,8,7,4,6};
 int b[size-1];
 int c[size-1];
 int arr2[] = {18,19,11,14,12};
   
void merginglist1(int low, int mid, int high) {
   int l1, l2, i;

   for(l1 = low, l2 = mid + 1, i = low; l1 <= mid && l2 <= high; i++) {
      if(arr1[l1] <= arr1[l2])
         b[i] = arr1[l1++];
      else
         b[i] = arr1[l2++];
   }
   
   while(l1 <= mid)    
      b[i++] = arr1[l1++];

   while(l2 <= high)   
      b[i++] = arr1[l2++];

   for(i = low; i <= high; i++)
      arr1[i] = b[i];
}

void merginglist2(int low, int mid, int high) {
   int l1, l2, j;

   for(l1 = low, l2 = mid + 1, j = low; l1 <= mid && l2 <= high; j++) {
      if(arr2[l1] <= arr2[l2])
         b[j] = arr2[l1++];
      else
         b[j] = arr2[l2++];
   }
   
   while(l1 <= mid)    
      b[j++] = arr2[l1++];

   while(l2 <= high)   
      b[j++] = arr2[l2++];

   for(j = low; j <= high; j++)
      arr2[j] = b[j];
}

void sort1(int low, int high) {
   int mid;
   
   if(low < high) {
      mid = (low + high) / 2;
      sort1(low, mid);
      sort1(mid+1, high);
      merginglist1(low, mid, high);
   } else { 
      return;
   }   
}

void sort2(int low, int high) {
   int mid;
   
   if(low < high) {
      mid = (low + high) / 2;
      sort2(low, mid);
      sort2(mid+1, high);
      merginglist2(low, mid, high);
   } else { 
      return;
   }   
}

int main(void) {
 
   
 
 
   int len1 = 5;
 
   int i=0,j=0;
    
    sort1(0, size);
    sort2(0, size);
   
   
 
   while(len1 > i && len1 > j){    //O(n)
 
      if (arr1[i] < arr2[j]) { 
          i++;
 
       }else if(arr2[j] < arr1[i]){
         j++;
 
       } else {
 
        printf("\nCommon element is %d\n",arr1[i]);
        i++;
        j++;
      }
   }
    
 
 
   return 0;
}