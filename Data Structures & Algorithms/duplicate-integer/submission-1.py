class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            #Check if lengths of original list equals the length of the set without duplicates
        return len(nums) != len(set(nums))
           