# @leet start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count characters in strings and comapre (form a dict)
        s_dict = {}
        t_dict = {}
        for c in s:
            if c not in s_dict:
                s_dict[str(c)] = 0
            s_dict[c] += 1
        for c in t:
            if c not in t_dict:
                t_dict[c] = 0
            t_dict[c] += 1
        return s_dict == t_dict

# @leet end
