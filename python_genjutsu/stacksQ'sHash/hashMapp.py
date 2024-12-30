from typing import List, Dict
from collections import deque

def get_counter(a:List[int]) -> Dict[int,int]:
    # init hashmap to store each number and its count

    counter:Dict[int,int] = {}

    for n in a:
        # check if n is a key in map

        if n in counter:
            counter[n] +=1
        else:
            counter[n] = 1
    return counter

def rotateLeftTillZero(n:List[int]) -> List[int]:
    queue = deque(n) # init queue of nums/n

    while queue[0] != 0:
        # remove the front element of the queue and it to the end
        queue.append(queue.popleft())
        #create a list out of queue
    return list(queue)


class Item(object):



    def __init__(self, key, value):

        self.key = key

        self.value = value

class HashTable(object):


    def __init__(self, size):

        self.size = size

        self.table = [[] for _ in range(self.size)]



    def _hash_function(self, key):

        return key % self.size



    def set(self, key, value):

        hash_index = self._hash_function(key)

        for item in self.table[hash_index]:

            if item.key == key:

                item.value = value

                return

        self.table[hash_index].append(Item(key, value))



    def get(self, key):

        hash_index = self._hash_function(key)

        for item in self.table[hash_index]:

            if item.key == key:

                return item.value

        raise KeyError('Key not found')



    def remove(self, key):

        hash_index = self._hash_function(key)

        for index, item in enumerate(self.table[hash_index]):

            if item.key == key:

                del self.table[hash_index][index]

                return

        raise KeyError('Key not found')