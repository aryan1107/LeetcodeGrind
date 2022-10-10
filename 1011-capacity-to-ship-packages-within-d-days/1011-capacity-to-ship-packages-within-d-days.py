class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = r
        while l<=r:
            mid = (l+r)//2
            curr = 0
            need = 1
            for w in weights:
                if w + curr > mid:
                    need += 1
                    curr = 0
                curr += w
            if need <= days:
                r = mid - 1
                res = min(res,mid)
            else:
                l = mid + 1
        return res