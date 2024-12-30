#include <iostream>
#include <stdexcept> // For exceptions

template <typename T>
class CustomVector {
private:
    T* data;            // Pointer to dynamically allocated array
    size_t capacity;    // Total allocated memory for the vector
    size_t size;        // Number of elements in the vector

    // Resize function to handle capacity doubling
    void resize() {
        capacity = (capacity == 0) ? 1 : capacity * 2;
        T* newData = new T[capacity];
        for (size_t i = 0; i < size; i++) {
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
    }

public:
    // Constructor
    CustomVector() : data(nullptr), capacity(0), size(0) {}

    // Destructor
    ~CustomVector() {
        delete[] data;
    }

    // Push an element to the back
    void push_back(const T& value) {
        if (size == capacity) {
            resize();
        }
        data[size++] = value;
    }

    // Remove the last element
    void pop() {
        if (size > 0) {
            size--;
        } else {
            throw std::out_of_range("Cannot pop from an empty vector");
        }
    }

    // Push an element to the front
    void push(const T& value) {
        if (size == capacity) {
            resize();
        }
        for (size_t i = size; i > 0; i--) {
            data[i] = data[i - 1];
        }
        data[0] = value;
        size++;
    }

    // Get the beginning iterator (pointer to the first element)
    T* begin() {
        return data;
    }

    // Get the ending iterator (pointer to one past the last element)
    T* end() {
        return data + size;
    }

    // Get size of the vector
    size_t getSize() const {
        return size;
    }

    // Access elements by index
    T& operator[](size_t index) {
        if (index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return data[index];
    }
};

int main() {
    CustomVector<int> vec;

    // Add elements using push_back
    vec.push_back(10);
    vec.push_back(20);
    vec.push_back(30);

    // Add element to the front using push
    vec.push(5);

    // Print elements
    std::cout << "Vector elements: ";
    for (auto it = vec.begin(); it != vec.end(); it++) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // Remove last element using pop
    vec.pop();

    // Print elements after pop
    std::cout << "After pop: ";
    for (auto it = vec.begin(); it != vec.end(); it++) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // Access elements by index
    std::cout << "Element at index 1: " << vec[1] << std::endl;

    return 0;
}
