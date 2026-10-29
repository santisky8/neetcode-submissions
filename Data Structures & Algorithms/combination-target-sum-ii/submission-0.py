class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        def backtrack(start, remain):
            if remain == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i])
                path.pop()
        backtrack(0, target)
        return result