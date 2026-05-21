class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        # keep track of the max left and max right
        # current water level depends on the max left and max right
        
        l,r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        total_water_levels = 0

        while l < r:
            if maxl < maxr:
                l += 1 # move the left pointer
                maxl = max(maxl, height[l]) # update to new potential max left
                total_water_levels += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                total_water_levels += maxr - height[r]
        return total_water_levels

        # time complexity: O(n) -> we just traverse through the entire array
        # space complexity: O(1)