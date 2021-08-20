import random
import time

# Comparison of naive search and binary search
# Naive pattern searching is th esimplest method of all pattern searching algorithms
# Binary search is a 'divide and conquer algorithm which requires the initial array to be sorted

# Binary search will be faster than naive search

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# for binary search the list must be sorted
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
    # example l = [1, 3, 5, 10, 12] # if target is 10, should return 3
    midpoint = (low + high) // 2 # 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else: 
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l,target))

    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

# time comparison of both search patterns
    start = time.time()
    for target in sorted_list: 
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds.")

    start = time.time()
    for target in sorted_list: 
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds.")


