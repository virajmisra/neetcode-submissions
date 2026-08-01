class Solution:
    def trap(self, height: List[int]) -> int:
        mL = height[0]
        mR = height[-1]
        l = 0 
        r = len(height) - 1
        res = 0

        while l <= r:
            if mL < mR:
                mL = max(mL,height[l])
                res += mL - height[l]
                l += 1
            else:
                mR = max(mR, height[r])
                res += mR - height[r]
                r -= 1
        return res