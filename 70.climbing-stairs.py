# @leet start
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp problem:
        # when you step up 1 or 2 steps,
        # the remaining steps is the same as a prior calculation if you memoize
        # therefore, for n steps, sum n-1 and n-2 ways to get n ways
        if n == 1:
            return 1
        ways = [0] * n
        # init first 2 steps
        ways[0] = 1
        ways[1] = 2
        for i in range(2, n):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[-1]

        
# @leet end
