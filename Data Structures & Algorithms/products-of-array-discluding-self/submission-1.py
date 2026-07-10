class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        # out = [48,24,12,8]
        # out[0] = pre[1]
        # out[-1] = post[len(post)-2]
        # everything else is pre[i-1] * post[i+1]
        pre = [0] * len(nums)
        pre[0] = nums[0]
        for i in range(1,len(pre)):
            pre[i] = pre[i-1] * nums[i]
        # pre = [1,2,8,48]

        post = [0] * len(nums)
        post[-1] = nums[-1]
        for i in range(len(post)-2,-1,-1):
            post[i] = post[i+1] * nums[i]
        # post = [48,48,24,6]

        res = [0] * len(nums)
        res[0] = post[1]
        res[-1] = pre[len(pre)-2]
        for i in range(1,len(nums)-1,1):
            res[i] = pre[i-1] * post[i+1]
        return res
            