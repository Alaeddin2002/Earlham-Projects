#include <stdio.h>
#include <limits.h>

int greedy(int val, int* coins, int n) {

  //TODO
  
  return -1;
}

int divide_and_conquer(int val, int* coins, int n, int* table) {

  //TODO

  return -1;
}

int dyn_prog(int val, int* coins, int n, int* table, int* sol) {

  //TODO

  return -1;
}

void print_sol(int val, int* sol) {

  //TODO
  
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
