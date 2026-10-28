class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = []
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] >= h:
                j, top = stack.pop()
                best = max(best, top * (i - j))
                start = j
            stack.append((start, h))
        return best