# @leet start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1
        while min <= max:
            mid = (max + min) // 2
            print(min, mid, max)
            print(f'{target} ? {nums[mid]}')
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                print('less than')
                max = mid - 1
            elif target > nums[mid]:
                print('greater than')
                min = mid + 1
            else:
                print("???")
        return -1
# @leet end
