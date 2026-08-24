class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_one = 2
        prev_two = 1
        current = 0

        for i in range(3, n + 1):
            current = prev_one + prev_two
            prev_two = prev_one
            prev_one = current

        return current