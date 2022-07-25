class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = 0
        e = len(nums)
        l = 0
        while s < e:
            m = (s+e)//2
            if nums[m] < target:
                s = m + 1
            else:
                e = m
        if s == len(nums) or nums[s] != target:
            return [-1,-1]
        l = s
        e = len(nums)
        while s < e:
            m = (s+e)//2
            if nums[m] <= target:
                s = m+1
            else:
                e = m
        return [l, e-1]