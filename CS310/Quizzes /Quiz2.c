// Ihsan Alaeddin
// October 7,2021 

#include <stdio.h>
// Got some help from https: www.geeksforgeeks.org/binary-search/

int Search(int arr[], int l, int r, int x) 
{ 
    if (r >= l) { 
        int mid = l + (r - l) / 2; 
        if (arr[mid] == x) 
            return mid; 
        if (arr[mid] > x) 
            return Search(arr, l, mid - 1, x); 
        return Search(arr, mid + 1, r, x); 
    } 
    return -1; 
}  
int main() 
{ 
    int arr[] = { 1, 4, 2, 6, 40 }; 
    int length = sizeof(arr) / sizeof(arr[0]);
    int temp = 0;
    int x = 1; 
    int result = Search(arr, 0, length - 1, x); 
    for (int i = 0; i < length; i++) {     
        for (int j = i+1; j < length; j++) {     
            if(arr[i] > arr[j]) {    
                 temp = arr[i];    
                 arr[i] = arr[j];    
                 arr[j] = temp;    
            }     
                }  
                    }
    (result == -1) ? printf("The element is not present in array") 
                   : printf("The element is present at index %d", 
                            result); 
    return 0; 
}

   
        
        
   