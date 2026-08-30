class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for l in matrix:
            for num in l:
                nums.append(num)
        
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False