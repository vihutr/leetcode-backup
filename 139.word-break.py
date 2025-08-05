# @leet start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dynamic programming problem
        # memoiz each usage of a word and each set of usages
        # recursion
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, memo)

    def dfs(self, s: str, wordSet, memo) -> bool:
        if s in memo:
            return memo[s]
        if s in wordSet:
            return True
        for i in range(1, len(s)):
            pre = s[:i]
            if pre in wordSet and self.dfs(s[i:], wordSet, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False



# @leet end
