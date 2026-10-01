class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        pre[0] = nums[0]
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i]
        
        post = [0] * len(nums)
        post[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            post[i] = post[i+1] * nums[i]
        
        res = [0] * len(nums)
        res[0] = post[1]
        res[-1] = pre[len(pre)-2]

        for i in range(1,len(res)-1):
            res[i] = pre[i-1] * post[i+1]
        return res
        