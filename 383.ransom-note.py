# @leet start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphaMap = {}
        for c in ransomNote:
            if c in alphaMap:
                alphaMap[c] += 1
            else:
                alphaMap[c] = 1
        print(alphaMap)
        for c in magazine:
            if c in alphaMap:
                alphaMap[c] -= 1
                if alphaMap[c] <= 0:
                    del alphaMap[c]
        print(alphaMap)
        if len(alphaMap) > 0:
            return False
        return True
# @leet end
