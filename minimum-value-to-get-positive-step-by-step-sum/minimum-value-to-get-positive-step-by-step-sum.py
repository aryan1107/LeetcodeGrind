class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])

        if min(prefix) <= 0:
            return abs(min(prefix))+1
        else:
            return 1