from typing import Dict, List

def execute(program: List[str]) -> List[int]:
    # initialize the stack
    stack: List[int] = []
    for instruction in program:
        if instruction == "peek":
            # print out the top item in stack
            print(stack[-1])
        elif instruction == "pop":
            # pop the top item in stack
            stack.pop()
        else:
            # get the data in the "push" instruction
            data = int(instruction[5:])
            # push data to the top of stack
            stack.append(data)
    return stack

def get_counter(arr: List[int]) -> Dict[int, int]:
    # initialize a hash map to store each number and its count
    counter: Dict[int, int] = {}
    for num in arr:
        # check if num is a key in the hash map
        if num in counter:
            # update the count of num to increase by 1
            counter[num] += 1
        else:
            # set the count of num to 1
            counter[num] = 1
    return counter


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

if __name__ == "__main__":
    program = [input() for _ in range(int(input()))]
    res = execute(program)
    print(" ".join(map(str, res)))