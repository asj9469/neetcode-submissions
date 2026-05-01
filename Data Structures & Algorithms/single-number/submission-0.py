class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # unoptimal solution -> keeping a frequency dictionary

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for k,v in freq.items():
            if v == 1:
                return k