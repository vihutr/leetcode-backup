# @leet start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        num_stack = []
        for t in range(len(tokens)):
            if tokens[t] in operators:
                n2 = num_stack.pop()
                n1 = num_stack.pop()
                result = 0
                if tokens[t] == '+':
                    result = n1 + n2
                elif tokens[t] == '-':
                    result = n1 - n2
                elif tokens[t] == '*':
                    result = n1 * n2
                elif tokens[t] == '/':
                    # division always truncates to zero so use // (floor divison)
                    # account for negative values by simply adding 1 when there is a remainder
                    result = n1 // n2
                    if result < 0 and n1 % n2 != 0:
                        result += 1
                # print(f'{tokens[t]} Operation Found')
                # print(f'Executed on {n1} and {n2}')
                # print(f'Result: {result}')
                num_stack.append(result)
            else:
                num_stack.append(int(tokens[t]))
                # print(f'Adding {tokens[t]} to Stack')
        return num_stack[0]
# @leet end
