class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = curr = 0
        ans = float('-inf')
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if k == 0:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                else:
                    k -= 1
            ans = max(ans, i-l+1)
        return ans