class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, temp in enumerate(nums):
            if i > 0 and temp == nums[i-1]: continue
            l, r = i + 1, len(nums)-1

            while l < r:
                if nums[l] + nums[r] + temp == 0:
                    res.append([temp,nums[l],nums[r]])
                    l+=1
                    # keep skipping until new one
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] + temp > 0:
                    r -= 1
                else:
                    l += 1
        return res