class Solution:

    def climbWithMemo(self, n, memo):
        if n == 0: # Valid steps reached top
            return 1
        if n < 0: # Invalid steps reached top
            return 0

        if (str(n) in memo):
            return memo[str(n)]

        num_ways = self.climbWithMemo(n-1, memo) + self.climbWithMemo(n-2, memo)
        memo[str(n)] = num_ways
        
        return num_ways

    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climbWithMemo(n, memo)
        