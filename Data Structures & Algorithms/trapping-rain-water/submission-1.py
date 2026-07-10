class Solution:
    def trap(self, height: List[int]) -> int:
        # l = 0, r = 1, 
        # if nums[l]>nums[r], we know 
        #   potentialHeight = nums[l]-nums[r]
        # water can be stored there
        # r += 1: while r < len(height) and nums[r] < nums[l]
        # potentialHeight += nums[r], r +=
        maxRights = {}
        mR = height[-1]
        maxRights[len(height)-1] = float("-inf")
        for i in range(len(height)-2,-1,-1):
            mR = max(mR,height[i])
            maxRights[i] = mR

        mL = height[0]
        maxLefts = {}
        maxLefts[0] = float("-inf")
        for i in range(1,len(height)):
            mL = max(mL,height[i])
            maxLefts[i] = mL
        
        res = 0
        for i in range(len(height)):
            num = min(maxLefts[i],maxRights[i]) - height[i]
            if num > 0:
                res += num
        return res
            