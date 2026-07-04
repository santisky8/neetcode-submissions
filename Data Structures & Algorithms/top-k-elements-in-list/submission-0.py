class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Count frequencies and create a map
        count_map = Counter(nums)
        
        #ask for the top elements in .most_common(2) and return them in brackets as specified above 
        top_pairs = count_map.most_common(k)

        #Strips out just the numbers and ignores the frequency count
        return [item[0] for item in top_pairs]