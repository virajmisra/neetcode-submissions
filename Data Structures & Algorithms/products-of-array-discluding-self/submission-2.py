class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0] * len(nums)
        prefixes[0] = nums[0]
        # [1,2,8,48]
        for i in range(1,len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i]
        
        postfixes = [0] * len(nums)
        postfixes[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            postfixes[i] = postfixes[i+1] * nums[i]
        # [48,48,24,6]
        
        res = [0] * len(nums)
        res[0] = postfixes[1]
        res[-1] = prefixes[len(prefixes)-2]
        for i in range(1,len(res)-1):
            res[i] = prefixes[i-1] * postfixes[i+1]
        return res

