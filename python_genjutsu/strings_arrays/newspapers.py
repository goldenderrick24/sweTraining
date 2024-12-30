from typing import List

def feasible(newspapers_read_times: List[int], num_coworkers: int, limit: int) -> bool:
    # time to keep track of the current worker's time spent, num_workers to keep track of the number of coworkers used
    time, num_workers = 0, 0
    for read_time in newspapers_read_times:
        # check if current time exceeds the given time limit
        if time + read_time > limit:
            time = 0
            num_workers += 1
        time += read_time
    # edge case to check if we needed an extra worker at the end
    if time != 0:
        num_workers += 1
    # check if the number of workers we need is more than what we have
    return num_workers <= num_coworkers

def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        # helper function to check if a time works
        if feasible(newspapers_read_times, num_coworkers, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

if __name__ == "__main__":
    newspapers_read_times = [int(x) for x in input().split()]
    num_coworkers = int(input())
    res = newspapers_split(newspapers_read_times, num_coworkers)
    print(res)