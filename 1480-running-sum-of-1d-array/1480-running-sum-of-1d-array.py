class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        curr = 0
        for i in nums:
            curr += i
            ans.append(curr)
        return ans
            