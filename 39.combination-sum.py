# @leet start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # if target - candidate < 0, all candidate of index > current i do not work for the current set
        result = []
        current_nums = []
        return self.fun(candidates, target, 0, 0, current_nums, result)
    
    # function for recursive checking of all possilbe sums
    # a form of DFS
    def fun(self, candidates, target, index, sum, current_nums, result):
        if sum == target:
            new_result = current_nums.copy()
            in_list = False
            for r in result:
                if set(new_result) == set(r):
                    in_list = True
            if not in_list:
                result.append(current_nums.copy())
        elif sum < target:
            for i in range(index, len(candidates)):
                current_nums.append(candidates[i])
                self.fun(candidates, target, i, sum + candidates[i], current_nums, result)
                current_nums.pop()
        return result
# @leet end
