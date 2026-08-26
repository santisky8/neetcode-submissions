class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            current_val = matrix[row][col]

            if current_val == target:
                return True

            elif current_val > target:
                right = mid - 1

            else:
                left = mid + 1

        return False
