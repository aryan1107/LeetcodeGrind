class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for j,i in enumerate(nums):
            diff = target - i
            if diff in hm:
                return [hm[diff], j]
            hm[i] = j