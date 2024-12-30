#include <iostream>
using namespace std;

/*Time Complexity Analysis:

Worst Case : O(n) 
Average Case: O(n) 
Best Case : O(n)
Auxiliary Space: O(1)

Advantage of Cycle sort:
No additional storage is required.
 in-place sorting algorithm.
 A minimum number of writes to the memory
 Cycle sort is useful when the array is stored in EEPROM or FLASH. 
Disadvantage  of Cycle sort:
 It is not mostly used.
 It has more time complexity o(n^2)
 Unstable sorting algorithm.
Application  of Cycle sort:
This sorting algorithm is best suited for situations where memory write or swap operations are costly.
Useful for complex problems. */

void cyclicSort(int arr[], int n){
int i = 0; 
while(i < n)
{
	// as array is of 1 based indexing so the
	// correct position or index number of each
	// element is element-1 i.e. 1 will be at 0th
	// index similarly 2 correct index will 1 so
	// on...
	int correct = arr[i] - 1 ;
	if(arr[i] != arr[correct]){

	// if array element should be lesser than
	// size and array element should not be at
	// its correct position then only swap with
	// its correct position or index value
	swap(arr[i], arr[correct]) ;
	}else{

	// if element is at its correct position
	// just increment i and check for remaining
	// array elements
	i++ ;
	}
}

}
/*Method 2: This method is only applicable when given array values or elements are in the range of 1 to N or  0 to N. In this method, we do not need to rotate an array

Approach : All the given array values should be in the range of 1 to N or 0 to N. If the range is 1 to N  then every array element’s correct position will be the index == value-1 i.e. means at the 0th index value will be 1 similarly at the 1st index position value will be 2 and so on till nth value.

similarly for 0 to N values correct index position of each array element or value will be the same as its value i.e. at 0th index 0 will be there 1st position 1 will be there.*/
void cycleSort(int arr[], int n)
{
    // count number of memory writes
    int writes = 0;
 
    // traverse array elements and put it to on
    // the right place
    for (int cycle_start = 0; cycle_start <= n - 2; cycle_start++) {
        // initialize item as starting point
        int item = arr[cycle_start];
 
        // Find position where we put the item. We basically
        // count all smaller elements on right side of item.
        int pos = cycle_start;
        for (int i = cycle_start + 1; i < n; i++)
            if (arr[i] < item)
                pos++;
 
        // If item is already in correct position
        if (pos == cycle_start)
            continue;
 
        // ignore all duplicate  elements
        while (item == arr[pos])
            pos += 1;
 
        // put the item to it's right position
        if (pos != cycle_start) {
            swap(item, arr[pos]);
            writes++;
        }
 
        // Rotate rest of the cycle
        while (pos != cycle_start) {
            pos = cycle_start;
 
            // Find position where we put the element
            for (int i = cycle_start + 1; i < n; i++)
                if (arr[i] < item)
                    pos += 1;
 
            // ignore all duplicate  elements
            while (item == arr[pos])
                pos += 1;
 
            // put the item to it's right position
            if (item != arr[pos]) {
                swap(item, arr[pos]);
                writes++;
            }
        }
    }
 
    // Number of memory writes or swaps
    // cout << writes << endl ;
}

void printArray(int arr[], int size)
{
int i;
for (i = 0; i < size; i++)
	cout << arr[i] << " ";
cout << endl;
}

int main() {

int arr[] = { 3, 2, 4, 5, 1};
int n = sizeof(arr) / sizeof(arr[0]);
cout << "Before sorting array: \n";
printArray(arr, n);
cyclicSort(arr, n);
cout << "Sorted array: \n";
printArray(arr, n);
return 0;

}
