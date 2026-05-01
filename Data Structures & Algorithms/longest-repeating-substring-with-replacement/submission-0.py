class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_freq = {}
        l = 0
        max_freq = 0

        for r in range(len(s)):
            rChar = s[r]
            window_freq[rChar] = window_freq.get(rChar, 0) + 1
            
            max_freq = max(max_freq, window_freq[rChar])

            window_size = r-l+1
            if window_size - max_freq > k: # we have to replace more than k to make it all the same
                # shrink
                lChar = s[l]
                window_freq[lChar] -= 1
                l += 1

        return r-l+1