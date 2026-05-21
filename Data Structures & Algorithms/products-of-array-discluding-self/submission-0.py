class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        running_prefix, running_postfix = 1, 1
        res = []

        for i in range(1, len(nums)):
            running_prefix *= nums[i-1]
            prefix[i] = running_prefix
        
        for i in range(len(nums)-2, -1, -1):
            running_postfix *= nums[i+1]
            postfix[i] = running_postfix

        for pre, post in zip(prefix, postfix):
            res.append(pre * post)

        return res