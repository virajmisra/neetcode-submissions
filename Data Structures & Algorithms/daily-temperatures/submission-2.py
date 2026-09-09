class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] # [temp,i]
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                j = stack[-1][1]
                res[j] = i - j
                stack.pop()
            stack.append([temperatures[i],i])
        return res
        