/** 	CS310 Project 3
File: make_change.c
Name: Ihsan Alaeddin
Date: Nibember 16,2021
*/  


#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

#define x  100

const int INF = 100000;
 int ans[x];
int o;
int greedy(int val, int* coins, int n) {

  //TODO
 
    int i,j,a, count = 0;
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            if (coins[i]>coins[j]){
                a = coins[i];
             coins[i] = coins[j];
             coins[j] = a;
          }
       }
    }
// take the highest values and substract them from the given value if they are higher than it
    for(i = 0; i < n; i++)
    {
        //take as much from coins[i]
        while(val >= coins[i])
        {
            //after taking the coin, reduce the value.
            val -= coins[i];
            ans[count] = coins[i];
            count++;
        }
        if(val == 0)
    return count;

    }

  return -1;
}

int divide_and_conquer(int val, int* coins, int n, int* table) {

  //TODO
    int step = 0;
    
     for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if (coins[i]>coins[j]){
                int a = coins[i];
             coins[i] = coins[j];
             coins[j] = a;
          }
       }
    }
    // if value in table
    if (table[val] > 0){
        return table[val];}
    if (val == 0){
        return 0;
    }
    
// if value higher than the first value by a lot decrease it
       
    if (val> coins[0]*2){
        while (val> coins[0]*2){
        val = val - coins[0];
        step = step + 1;
        }
        if (coins[0]>=50 ){
            val = val - coins[0];
            step = step + 1;
        }
    }
     
   
        int result = INT_MAX;
// find minimum steps using recursion

        for (int i = 0; i < n; i++){
            if (coins[i] <= val){
                int result2 = divide_and_conquer(val - coins[i],coins,n,table);
                if (result2 != INT_MAX && result2 + 1 < result){
                    result = result2 + 1;
                }
            }
           
        }
    if (result + step != 0 || result + step != INT_MAX + step ){
        table[val] = result + step;
        return table[val];
    }

    if ((result != 0 && result != INT_MAX) || (result == 0 && step != 0) || (result != 0 && result != INT_MAX && step != 0)){
        table[val] = result + step;
        return table[val];
    }

    return -1;
}

int dyn_prog(int val, int* coins, int n, int* table, int* sol) {
    
    int i,a,j;
    if (val>=0){
        for(i = 1; i <= val; i++){
            a = -1;
            for(j = 0; j<n; j++){
                if((table[i-coins[j]] < a || a == -1) && (coins[j]<=i) && table[i-coins[j]]!=-1){
                    a = table[i-coins[j]];
                    sol[i] = coins[j];
                }
            }
            if (a!=-1){
                table[i] = a +1;
            }
        }
    }
    else{
        return -1;
    }
    return table[val];
}

    
    


void print_sol(int val, int* sol) {
    int coin;
        while(val>0){
            coin = sol[val];
            printf("%d\n",coin);
            val = val - coin;
        }

  
}

int main(int argc, char** argv) {
  int n = argc - 2;
  int val;
  sscanf(argv[argc-1], "%d", &val);
  int coins[n];
  
  for(int i=0; i < n; i++) {
    sscanf(argv[i+1], "%d", &coins[i]);
  }

  printf("Making change for %d.\n", val);

  int res;

  res = greedy(val, coins, n);

  if(res != -1) {
	printf("Greedy found change using %d coins.\n", res);
  } else {
	printf("Greedy could not find change.\n");
  }

  int table[val+1];

  for(int i=0; i < val+1; i++) {
	table[i] = -1;
  }
  table[0] = 0;
  
  res = divide_and_conquer(val, coins, n, table);
  if (val<coins[n]){
      printf("Divide & conquer could not find change.\n");
  }
  if(res != -1) {
	printf("Divide & conquer found change using %d coins.\n", res);
  } else {
	printf("Divide & conquer could not find change.\n");
  }

  int sol[val+1];
  for(int i=0; i < val+1; i++) {
	table[i] = -1;
	sol[i] = -1;
  }
  table[0] = 0;
  sol[0] = 0;
  
  res = dyn_prog(val, coins, n, table, sol);
  
  if(res != -1) {
	printf("Dynamic programming found change using %d coins.\n", res);
	print_sol(val, sol);
  } else {
	printf("Dynamic programming could not find change.\n");
  }
}

 