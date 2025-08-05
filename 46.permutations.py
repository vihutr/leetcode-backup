# @leet start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # the amount of permutations is len(nums) factorial
        # effectively need a len(nums) for loops
        if len(nums) == 1:
            return [nums[:]]
        
        results = []
        # dfs of taking out each element
        # ex: start loop, after taking out 1, branch off to taking out 2 first then 3, and 3 first then 2
        # next in loop, take out 2, do same with reamining 1 and 3, so on.
        # can do this by popping the elemnt out of (a copy of) the list of nums each time
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            print(perms)
            for p in perms:
                p.append(n)
            
            results.extend(perms)
            nums.append(n)
        return results
# @leet end
