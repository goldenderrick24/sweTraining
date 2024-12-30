from typing import List
"""
Find the first true in a sorted boolean array
"""
def find_boundary(a:List[bool]) -> int:
    l,r = 0, len(a)-1
    boundaryIdx = -1

    while l <=r:
        mid = (l+r) // 2
        if a[mid]:
            boundaryIdx = mid
            r = mid - 1
        else:
            l = mid+1
        
    return boundaryIdx

def firstNotSmaller(a:List[int], target:int) -> int:
    l,r = 0, len(a)-1
    bIdx = -1

    while l <= r:
        mid = (l+r) // 2
        if a[mid] >= target:
            bIdx = mid
            r = mid -1
        else:
            l = mid + 1
    return bIdx

def firstOccurence(a:List[int], target:int) -> int:
    l,r = 0, len(a) - 1
    ans = -1
    while l<=r:
        mid = (l+r) // 2
        if a[mid] == target:
            ans = mid
            r = mid -1
        elif a[mid] < target:
            l = mid + 1
        else:
            r = mid -1
    return ans

def squareRootEst(n:int) -> int:
    if n == 0:
        return 0
    
    l = -1
    r = n
    res = -1
    while l<=r:
        mid = (l+r) //2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            res = mi
            r = mid -1
        else:
            l = mid + 1
    return res - 1