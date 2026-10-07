class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # middle row is numRows-2 if numRows >= 3
        # for numRows < 3, no diagonal

        # list -> keep track of current chunk
        temp = []
        diagCount = numRows - 2

        i = 0
        while i < len(s):
            # mainChunk = s[i:i+numRows]
            temp.append(s[i:i+numRows])
            i = i+numRows

            # diagChunk
            if numRows >= 3:
                j = 1
                while i < len(s) and j <= diagCount:
                    temp.append((" " * (numRows-j-1)) + s[i] + (" " * j))
                    i += 1
                    j += 1
        print(temp)
        maxStrLen = max(len(w) for w in temp)
        sumStrLen = sum(len(w) for w in temp)

        total, curr = 0,0
        newString = ""
        while total < sumStrLen:
            for w in temp:
                if curr < len(w):
                    newString += w[curr].strip()
                    total += 1
                else:
                    # last column
                    newString += ""
            curr += 1
        return newString
