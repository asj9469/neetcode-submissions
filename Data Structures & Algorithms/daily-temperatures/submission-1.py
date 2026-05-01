class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [0 for _ in range(len(temperatures))]

        # # brute force method
        # for i in range(len(temperatures)):
        #     curr = temperatures[i]
        #     count = 1
        #     for j in range(i + 1, len(temperatures)):
        #         if curr >= temperatures[j]:
        #             count += 1
        #         else:
        #             print(count)
        #             res[i] = count
        #             break
        
        # return res

        # stack method
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, val in enumerate(temperatures):
            while stack:
                if val > stack[-1][0]:
                    index = stack[-1][1]
                    res[index] = i - index
                    stack.pop()
                else:
                    break
            stack.append((val, i))
        
        return res

