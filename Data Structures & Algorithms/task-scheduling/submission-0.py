class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        top = max(counts)
        tied = sum(1 for c in counts if c == top)
        return max(len(tasks), (top - 1) * (n + 1) + tied)