class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = min(nums), sum(nums)
        res = r
        while l<=r:
            mid = (l+r)//2
            curr, split = 0, 1
            for n in nums:
                if n > mid:
                    split = k + 1
                    break
                if n + curr > mid:
                    split +=1
                    curr = 0
                curr += n
            
            if split <= k:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
        