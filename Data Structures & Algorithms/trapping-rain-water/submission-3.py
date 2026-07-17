class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        mL = height[l]
        mR = height[r]
        res = 0
        while l < r:
            if mL < mR:
                l += 1
                mL = max(height[l],mL)
                res += mL - height[l]
            else:
                r -= 1
                mR = max(height[r],mR)
                res += mR - height[r]
        return res