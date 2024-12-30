/*Approach: To solve the problem follow the given steps:

Declare a new array prefixSum[] of the same size as the input array
Run a for loop to traverse the input array
For each index add the value of the current element and the previous value of the prefix sum array
Applications of Prefix Sum: 
Equilibrium index of an array: The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
Find if there is a subarray with 0 sums: Given an array of positive and negative numbers, find if there is a subarray (of size at least one) with 0 sum.
Maximum subarray size, such that all subarrays of that size have a sum less than k: Given an array of n positive integers and a positive integer k, the task is to find the maximum subarray size such that all subarrays of that size have the sum of elements less than k.
Find the prime numbers which can be written as sum of most consecutive primes: Given an array of limits. For every limit, find the prime number which can be written as the sum of the most consecutive primes smaller than or equal to the limit.
Longest Span with same Sum in two Binary arrays: Given two binary arrays, arr1[] and arr2[] of the same size n. Find the length of the longest common span (i, j) where j >= i such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j].
Maximum subarray sum modulo m: Given an array of n elements and an integer m. The task is to find the maximum value of the sum of its subarray modulo m i.e find the sum of each subarray mod m and print the maximum value of this modulo operation.
Maximum occurred integer in n ranges : Given n ranges of the form L and R, the task is to find the maximum occurring integer in all the ranges. If more than one such integer exits, print the smallest one.
Minimum cost for acquiring all coins with k extra coins allowed with every coin: You are given a list of N coins of different denominations. you can pay an amount equivalent to any 1 coin and can acquire that coin. In addition, once you have paid for a coin, we can choose at most K more coins and can acquire those for free. The task is to find the minimum amount required to acquire all the N coins for a given value of K.
Random number generator in arbitrary probability distribution fashion: Given n numbers, each with some frequency of occurrence. Return a random number with a probability proportional to its frequency of occurrence.
*/// C++ program for Implementing prefix sum array

#include <bits/stdc++.h>
using namespace std;

// Fills prefix sum array
void fillPrefixSum(int arr[], int n, int prefixSum[])
{
	prefixSum[0] = arr[0];
	// Adding present element with previous element
	for (int i = 1; i < n; i++)
		prefixSum[i] = prefixSum[i - 1] + arr[i];
}

// Driver Code
int main()
{
	int arr[] = { 10, 4, 16, 20 };
	int n = sizeof(arr) / sizeof(arr[0]);
	int prefixSum[n];

	// Function call
	fillPrefixSum(arr, n, prefixSum);
	for (int i = 0; i < n; i++)
		cout << prefixSum[i] << " ";
}

// This code is contributed by Aditya Kumar (adityakumar129)
