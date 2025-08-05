# @leet start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # if a version x is good and version x+1 is bad,
        # x+1 is the first bad version
        # n is the last version, so the domain is constrained to n
        # using a sldiing window w/ 2 pts method in a loop
        # without checking around the divides requires us to manually check 1
        if n == 1:
            return n
        minimum = 0
        maximum = n
        result = -1
        while maximum >= minimum:
            n = (maximum + minimum) // 2
            bad = isBadVersion(n)
            if bad:
                maximum = n - 1
                result = n
            else:
                minimum = n + 1
        return result

# @leet end
