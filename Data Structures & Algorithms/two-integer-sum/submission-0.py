class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, n in enumerate (nums):

            needed_number = target - n 

            if needed_number in seen:

                return [seen[needed_number], i]

            seen[n] = i


