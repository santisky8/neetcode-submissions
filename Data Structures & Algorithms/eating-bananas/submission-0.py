import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = left + (right - left) // 2

            total_hours = sum((pile - 1) // mid + 1 for pile in piles)

            if total_hours <= h:
                right = mid - 1

            else:
                left = mid + 1
        
        return left



