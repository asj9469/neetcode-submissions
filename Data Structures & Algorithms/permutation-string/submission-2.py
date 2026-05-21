class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 character count stay static
        # need to compare window on s2, fixed window count

        if len(s1) > len(s2): return False
        s1count = [0] * 26
        s2count = [0] * 26

        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] +=1
            s2count[ord(s2[i]) - ord('a')] +=1
        
        # at this point we have character counts for the 1st fixed size window
        if s1count == s2count:
            return True

        # now move around the fixed size window
        l = 0
        for r in range(len(s1), len(s2)):
            # count up the newly added character
            rChar = s2[r]
            s2count[ord(rChar)-ord('a')] += 1

            lChar = s2[l]
            s2count[ord(lChar) - ord('a')] -= 1
            l += 1

            if s1count == s2count:
                return True

        return False