import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    rev_nums = []

    for num in nums:
        heapq.heappush(rev_nums, -num)

    result = []
    while rev_nums:
        result.append(-heapq.heappop(rev_nums))

    return result





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
