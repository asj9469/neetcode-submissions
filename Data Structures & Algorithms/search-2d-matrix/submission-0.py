class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first define the search space
        l, r = 0, len(matrix)-1
        i = 0
        # find the correct subarray first
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                i = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            
        # now binary search inside the subarray
        l2, r2 = 0, len(matrix[i])-1

        while l2 <= r2:
            mid2 = (l2 + r2) // 2
            curr = matrix[i][mid2]
            if curr == target:
                return True
            elif curr > target:
                r2 = mid2 - 1
            elif curr < target:
                l2 = mid2 + 1

        return False