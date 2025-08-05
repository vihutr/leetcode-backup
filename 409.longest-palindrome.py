# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # count how many pairs of letters there are
        # make a mapping of each letter found and add to count, then loop dict
        # check if there is at least 1 letter with no pair, if so add 1 to length
        map = {}
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        length = 0
        addone = False
        for key in map:
            print(key)
            print(map[key])
            print(
            length += map[key] // 2
            if map[key] % 2 == 1 and not addone:
                addone = True
        length = length * 2
        if addone:
            length += 1
        return length
# @leet end
