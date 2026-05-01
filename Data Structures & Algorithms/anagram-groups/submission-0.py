from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def createSerial(s):
            count = ['0'] * 26

            for c in s:
                position = ord(c) - ord('a')
                count[position] = str(int(count[position]) + 1)
            
            serial = ','.join(count)
            return serial

        wordMap = defaultdict(list)

        for s in strs:
            serial = createSerial(s)
            wordMap[serial].append(s)

        print(list(wordMap.values()))
        return list(wordMap.values())