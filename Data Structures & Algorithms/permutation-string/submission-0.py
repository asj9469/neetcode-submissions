class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation -> any combination of the unique characters -> have same unique characters
        # -> letter frequency is equal

        # for the fixed window size, we need to check if we have the same letter count

        # serialize method to create serials
        def serialize(s):
            word_count = ['0'] * 26
            
            for c in s:
                pos = ord(c.lower()) - ord('a')
                word_count[pos] = str(int(word_count[pos]) + 1)
            
            serial = ''.join(word_count)
            return serial

        # get the serial for s1 (generate a counter)
        s1_serial = serialize(s1)
        
        # check if the current window has same frequency count
        # fixed window size => length of s1
        
        l, r = 0, len(s1)-1
        for r in range(len(s1)-1, len(s2)):
            curr_string = s2[l:r+1]
            curr_serial = serialize(curr_string)
            if curr_serial == s1_serial:
                return True

            l += 1
        return False
                
            
            

            
            
