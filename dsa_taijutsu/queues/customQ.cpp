#include <iostream>
#include <stdexcept>
using namespace std;

template <typename T>
class Queue {
private:
    T* arr;
    int front;
    int rear;
    int capacity;
    int size;

public:
    Queue(int capacity = 10) : capacity(capacity), size(0), front(0), rear(-1) {
        arr = new T[capacity];
    }

    ~Queue() {
        delete[] arr;
    }

    void enqueue(T data) {
        if (size == capacity) {
            throw overflow_error("Queue is full");
        }
        rear = (rear + 1) % capacity;
        arr[rear] = data;
        size++;
    }

    T dequeue() {
        if (isEmpty()) {
            throw underflow_error("Queue is empty");
        }
        T data = arr[front];
        front = (front + 1) % capacity;
        size--;
        return data;
    }

    bool isEmpty() const {
        return size == 0;
    }

    int getSize() const {
        return size;
    }

    T peek() const {
        if (isEmpty()) {
            throw underflow_error("Queue is empty");
        }
        return arr[front];
    }
};

#include <iostream>
#include <stdexcept>
using namespace std;

template <typename T>
class Dequeue {
private:
    T* arr;
    int front;
    int rear;
    int capacity;
    int size;

public:
    Dequeue(int capacity = 10) : capacity(capacity), size(0), front(0), rear(-1) {
        arr = new T[capacity];
    }

    ~Dequeue() {
        delete[] arr;
    }

    void addFront(T data) {
        if (size == capacity) {
            throw overflow_error("Dequeue is full");
        }
        front = (front - 1 + capacity) % capacity;
        arr[front] = data;
        size++;
    }

    void addRear(T data) {
        if (size == capacity) {
            throw overflow_error("Dequeue is full");
        }
        rear = (rear + 1) % capacity;
        arr[rear] = data;
        size++;
    }

    T removeFront() {
        if (isEmpty()) {
            throw underflow_error("Dequeue is empty");
        }
        T data = arr[front];
        front = (front + 1) % capacity;
        size--;
        return data;
    }

    T removeRear() {
        if (isEmpty()) {
            throw underflow_error("Dequeue is empty");
        }
        T data = arr[rear];
        rear = (rear - 1 + capacity) % capacity;
        size--;
        return data;
    }

    bool isEmpty() const {
        return size == 0;
    }

    int getSize() const {
        return size;
    }
};

int main() {
    Dequeue<int> dq(5);
    dq.addRear(10);
    dq.addRear(20);
    dq.addFront(5);

    cout << "Remove front: " << dq.removeFront() << endl;
    cout << "Remove rear: " << dq.removeRear() << endl;

    return 0;
}

