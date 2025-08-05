# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window of 2 ptrs
        left = 0
        res = 0
        current_str = s[left:0]
        for right in range(len(s)):
            c = s[right]
            print(f'checking if {c} in {current_str}')
            if c in current_str:
                left += current_str.index(c) + 1
                print('found in str, new left: ' + str(left))
            current_str = s[left:right + 1]
            res = max(res, len(current_str))
            print(current_str, res)
            right += 1
        return res
# @leet end
