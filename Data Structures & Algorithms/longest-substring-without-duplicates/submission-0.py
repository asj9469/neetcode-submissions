class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # move along until we find a character we already saw
        maxLen = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxLen = max(maxLen, r - l + 1)
    
        return maxLen