# @leet start
class Solution:
    def trap(self, height: List[int]) -> int:
        # create pointers for each side
        # keep track of current heighest on each side
        # make decisions on whcih ptr to move based on max
        # because the lower height between two maxes deteermines the limit on water when moving inwards
        # we move the ptr that is smaller at any point
        result = 0
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                result += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                result += r_max - height[r]
        return result
# @leet end
