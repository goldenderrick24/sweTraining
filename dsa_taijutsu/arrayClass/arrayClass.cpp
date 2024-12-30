#include "bits/stdc++.h"
using namespace std;

// Function to rotate vector
void rotateArr(vector<int>& arr, int d) {
    int n = arr.size();  // Get the size of the array

    // Handle case when d > n (if d is larger than the array size)
    d %= n;
  
    // Storing rotated version of array in temp
    vector<int> temp(n);

    // Copy last d elements to the front of temp
    for (int i = 0; i < d; i++) 
        temp[i] = arr[n - d + i];

    // Copy the first n - d elements to the back of temp
    for (int i = 0; i < n - d; i++) 
        temp[i + d] = arr[i];

    // Copying the elements of temp in arr to get the final rotated vector
    for (int i = 0; i < n; i++) 
        arr[i] = temp[i];
};

void reverseArray(vector<int>& arr){
        int start = 0;
        int end = arr.size()-1;
        while(start<end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }                                                              
};

vector<int> leaders(vector<int>& arr){
    vector<int> res;
    int n = arr.size();
    int maxRight = arr[n-1];
    res.push_back(maxRight);
    for(int i = n-2; i>0;i--){
        if(arr[i]>maxRight){
            maxRight = arr[i];
            res.push_back(maxRight);
        }  
    } 
    reverseArray(res);
    return res;
};

int maxSubarray(vector<int>& arr){
    int res = arr[0], maxEnding = arr[0];
    for(int i = 1; i<arr.size(); i++){
        maxEnding = max(maxEnding + arr[i],arr[i]);
        res = max(res, maxEnding);
    }
    return res;
}

void swapVectorElements(vector<int>& vec, int index1, int index2) {
    // Check if indices are within bounds
    if (index1 >= 0 && index1 < vec.size() && index2 >= 0 && index2 < vec.size()) {
        // Swap the elements at index1 and index2
        int temp = vec[index1];
        vec[index1] = vec[index2];
        vec[index2] = temp;
    } else {
        cout << "Invalid indices!" << endl;
    }
};

void generateSubarrays(vector<int>& arr, int start, int end) {
    // Base case: If start exceeds the size of the array, stop recursion
    if (start == arr.size()) return;

    // If end exceeds the size of the array, reset end to start+1
    if (end == arr.size()) {
        generateSubarrays(arr, start + 1, start + 1);
        return;
    }

    // Print the current subarray
    for (int i = start; i <= end; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Recursive call to expand the current subarray
    generateSubarrays(arr, start, end + 1);
};

int main() {
    vector<int> arr = { 1, 2, 3, 4, 5, 6 };  // Initial array
    int d = 2;  // Number of positions to rotate

    rotateArr(arr, d);  // Rotate the array by d positions

    // Print the rotated array
    for (int i = 0; i < arr.size(); i++) 
        cout << arr[i] << " ";

    return 0;
}
