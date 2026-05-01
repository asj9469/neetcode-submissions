class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        # if same
        if word == abbr:
            return True

        # index
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            # get the number between 
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                numStr = ""
                while j < len(abbr) and abbr[j].isdigit():
                    numStr += abbr[j]
                    j += 1
                i += int(numStr)
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)