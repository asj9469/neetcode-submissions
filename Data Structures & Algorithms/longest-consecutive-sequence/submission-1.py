class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # cannot sort
        # create a dictionary with all entries
        sett = set(nums)
        longest, temp = 0, 0

        for i in nums:
            if i-1 not in sett:
                curr = i
                temp = 1
                while curr + 1 in sett:
                    curr += 1
                    temp += 1
                longest = max(longest, temp)
            
        return longest