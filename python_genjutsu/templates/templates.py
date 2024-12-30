

"""
Depth-First Search (DFS)
Scenario: Find All Paths in a Graph
Use DFS to find all paths from a source to a destination in a directed graph.
"""
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:  # Prevent cycles
            new_paths = find_all_paths(graph, neighbor, end, path)
            for p in new_paths:
                paths.append(p)

    return paths

# Example Usage
graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D"],
    "D": []
}
print(find_all_paths(graph, "A", "D"))
# Output: [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]



"""
Breadth-First Search (BFS)
Scenario: Shortest Path in a Grid
Find the shortest path from the top-left 
corner to the bottom-right corner of a 
binary grid (0 = empty, 1 = blocked).

"""

from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = set((0, 0))

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1  # Path not found

# Example Usage
grid = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 0]
]
print(shortest_path(grid))  # Output: 5



"""
subset generation
"""

def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])  # Add a copy of the current subset

        for i in range(start, len(nums)):
            current.append(nums[i])  # Include nums[i]
            backtrack(i + 1, current)  # Explore further
            current.pop()  # Exclude nums[i]

    backtrack(0, [])
    return result

# Example Usage
nums = [1, 2, 3]
print(subsets(nums))
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


"""
sliding window
"""

from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""

    t_count = Counter(t)
    window_count = {}
    have, need = 0, len(t_count)
    left, res, res_len = 0, [-1, -1], float("inf")

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in t_count and window_count[char] == t_count[char]:
            have += 1

        while have == need:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""

# Example Usage
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"


"""
heaps and priority queues
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):  # Comparison for the heap
        return self.val < other.val

def merge_k_lists(lists):
    min_heap = []
    for head in lists:
        if head:
            heapq.heappush(min_heap, head)

    dummy = ListNode()
    current = dummy

    while min_heap:
        node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, node.next)

    return dummy.next

# Example Usage
# Create example linked lists: [1->4->5], [1->3->4], [2->6]
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
merged = merge_k_lists([list1, list2, list3])

while merged:
    print(merged.val, end=" -> ")
    merged = merged.next
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 ->

"""
Two-Pointer Technique
Scenario: Longest Palindromic Substring
Find the longest palindromic substring in a given string.
"""
def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    result = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i+1)
        result = max(result, odd_palindrome, even_palindrome, key=len)

    return result

# Example Usage
s = "babad"
print(longest_palindrome(s))  # Output: "bab" or "aba"

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):  # Build a max heap
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)

# Example Usage
arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print(arr)  # Output: [1, 3, 4, 5, 10]

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example Usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]

"""
DFS and BFS on a tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_tree(root):
    if root is None:
        return
    print(root.val, end=" ")
    dfs_tree(root.left)
    dfs_tree(root.right)

# Example Usage
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
dfs_tree(root)  # Output: 1 2 3 4 5


from collections import deque

def bfs_tree(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example Usage
bfs_tree(root)  # Output: 1 2 3 4 5


"""
matrix operations/ dfs

"""
def find_path(matrix, visited, i, j, path):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0 or visited[i][j]:
        return False

    visited[i][j] = True
    path.append((i, j))

    if (i, j) == (len(matrix) - 1, len(matrix[0]) - 1):
        return True

    if find_path(matrix, visited, i + 1, j, path) or find_path(matrix, visited, i, j + 1, path):
        return True

    path.pop()
    visited[i][j] = False
    return False

# Example Usage
matrix = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]
visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
path = []
find_path(matrix, visited, 0, 0, path)
print(path)  # Output: [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]

