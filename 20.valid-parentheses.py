# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        # solve using a stack
        stack = []
        push = ['(', '{', '[']
        pop = [')', '}', ']']
        # loop through string
        for c in s:
            # open bracket
            if c in push:
                stack.append(c)
            # closed bracket
            # never append closing brackets = never compare closed bracket index
            elif c in pop:
                # edge case for closed bracket at start
                if len(stack) > 0:
                    # ensure matching closing bracket
                    if push.index(stack[-1]) == pop.index(c):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        # check after looping if stack is empty
        if not stack:
            return True
        return False
# @leet end
