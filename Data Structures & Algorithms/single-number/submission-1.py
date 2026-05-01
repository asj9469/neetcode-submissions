class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # sliding window?
        # as soon as we see a duplicate, we can adjust left pointer until duplicate is gone
        # by the end, left pointer will signify single number

        # 3, 2, 3
        #    l  r
        res = 0
        for n in nums:
            res ^= n
        
        return res