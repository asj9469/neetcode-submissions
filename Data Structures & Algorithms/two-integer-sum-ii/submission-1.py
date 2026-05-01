class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            summ = numbers[l] + numbers[r] 
            if summ == target:
                return [l+ 1, r+1]
            elif summ > target:
                # curr too big, we need to reduce
                r -= 1
            elif summ < target:
                # curr too small, might want to increase
                l += 1