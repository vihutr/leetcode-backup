# @leet start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        count = 0
        for n in nums:
            if count == 0:
                element = n
            if n == element:
                count += 1
            else:
                count -= 1
        return element
# @leet end
