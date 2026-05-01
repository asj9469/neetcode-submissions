class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # search space -> eating rate
        left, right = 1, max(piles)
    
        def feasible(rate):
            hour_count = 0

            for i in range(len(piles)):
                hour_count += (piles[i] + rate - 1) // rate
            
            if hour_count <= h:
                print(f"{h} is feasible at rate of {rate}")
                print(f"hour count was {hour_count}")
            return hour_count <= h

        while left < right:
            mid = (left + right)//2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        