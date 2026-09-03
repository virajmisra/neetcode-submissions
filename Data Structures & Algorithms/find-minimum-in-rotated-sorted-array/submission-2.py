class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return min(nums[l],res)

            m = (l+r) // 2

            res = min(res,nums[m])
            if nums[m] < nums[r]:
                r = m - 1 
            else:
                l = m + 1
        return res
