class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] # [i,temperature]
        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                j, t = stack.pop()
                res[j] = i - j
            stack.append([i,temperatures[i]])
        return res
        