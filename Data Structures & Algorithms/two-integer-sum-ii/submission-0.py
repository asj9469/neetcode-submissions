class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # define the search space
        l, r = 0, len(numbers) - 1
        
        while l < r:
            summ = numbers[l] + numbers[r] 
            if summ == target:
                return [l+1,r+1]
            
            if summ > target: # too big
                r -= 1
            else:
                l += 1
            
        return [l+1,r+1]
