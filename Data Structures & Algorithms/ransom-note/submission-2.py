class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # if magazine has overflow -> fine
        # if magazine runs out of characters -> instant false

        # construct hashmap for magazine frequency count (scope out resources)
        # subtract as we go through ransomNote

        freq = {}
        for c in magazine:
            freq[c] = freq.get(c, 0) + 1
        
        for i in ransomNote:
            if i in freq:
                freq[i] -= 1
                if freq[i] < 0:
                    return False
            else:
                return False
        return True