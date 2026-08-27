class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start_index: int, current_combination: list[int], current_sum: int):          
            if current_sum == target:
                result.append(list(current_combination))
                return
            
            if current_sum > target:
                return
            
            for i in range(start_index, len(nums)):
                current_combination.append(nums[i])
                
                backtrack(i, current_combination, current_sum + nums[i])
                
                current_combination.pop()
                
        backtrack(0, [], 0)
        return result