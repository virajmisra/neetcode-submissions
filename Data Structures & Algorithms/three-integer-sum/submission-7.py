class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4]
        # = [-4,-3,-2,-1,-1,0,0,1,2,3,4]
        i = 0
        while i < (len(nums)):
            while i > 0 and i < len(nums) and nums[i] == nums[i-1]:
                i+=1
            l = i + 1
            r = len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
                while l < r and l != i+1 and nums[l] == nums[l-1]:
                        l+=1
            i+=1
        return res