from typing import Dict, List

def insertionSort(a:List[int]) -> List[int]:
    n = len(a)

    for i in range(n):
        while i>0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1],a[i]
            i-=1
    return a

def efficientSort(a:List[int]) -> List[int]:
    for i in range(1,len(a)):
        key = a[i] # holds value at index
        j = i-1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j] # shifts values to the right
            j -= 1
        a[j + 1] = key # place key in correct position

# practice sorts
# practice trees
# practice stacks/queues/LL's
# practice strings
# practice templates
# practice heaps



            