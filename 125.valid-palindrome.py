# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = s.lower()
        new_phrase = ''
        for c in phrase:
            if c.isalnum():
                new_phrase = new_phrase + c
        print(new_phrase)
        half = len(new_phrase) // 2
        ptr = -1
        for i in range(half):
            if new_phrase[i] != new_phrase[ptr]:
                return False
            ptr -= 1
        return True
# @leet end
