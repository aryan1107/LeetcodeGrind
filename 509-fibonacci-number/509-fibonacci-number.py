class Solution:
    def fib(self, n: int) -> int:
        def helper(n):
            if n in memo:
                return memo[n]
            if n <2:
                return memo[n]
            ans = helper(n-1) + helper(n-2)
            return ans
        
        memo = {0:0, 1:1, 2:1}
        final = helper(n)
        return final