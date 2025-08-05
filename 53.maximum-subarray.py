# @leet start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highest_sum = nums[0]
        current_subarray_sum = 0
        for n in nums:
            current_subarray_sum += n
            if highest_sum < current_subarray_sum:
                highest_sum = current_subarray_sum
            if current_subarray_sum < 0:
                current_subarray_sum = 0
        return highest_sum


# @leet end
