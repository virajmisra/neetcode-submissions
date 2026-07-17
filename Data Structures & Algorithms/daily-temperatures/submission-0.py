class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                tt, ind = stack.pop()
                res[ind] = i - ind
            stack.append((t,i))
        return res