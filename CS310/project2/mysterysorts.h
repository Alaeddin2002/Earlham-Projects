#ifndef _mysterysorts_h
#define _mysterysorts_h
//#include <time>
#include <unistd.h>
#include <stdbool.h>

/* 
 * This function will perform one of several algorithms to sort an 
 * array of integers into ascending order. You can select the algorithm 
 * by providing a different value for the third argument (0 through 5.)
 * Each uses a different sorting algoritm, and therein lies the mystery!
 *
 * The fourth argument is a value that limits the sort to a given
 * number of "steps." What a step means differs by algorithm.
 * The function will return after that many steps have completed, 
 * even if the sorting hasn't been finished. By choosing an appropriate stop, 
 * you can examine the data mid-sort, which allows you to look for patterns in 
 * how the data is being rearranged. Providing a value of -1 for maxSteps
 * indicates the sort should be run to completion.
 */


void mysterySort(int* arr, int n, int sort, int maxSteps);

#endif
