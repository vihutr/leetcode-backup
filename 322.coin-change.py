# @leet start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ex: [2, 5, 7], 22
        # given an amount n max output is n
        # dp problem, calc all amounts up to amount asked for
        # store min coins necessary for each and check each
        # when you calc for n, n+x can reference n when a coin x is used
        # so long as each resut from 0 to n has been memoized

        # beacause whatever combination of coins must exactly = amount
        # initialize as amount + 1 so we can use min when making comparisons
        # offset by 1 to make index correspond to amount
        min_coins = [amount + 1] * (amount + 1)
        # deal with 0 cond, always 0 coins to make 0
        min_coins[0] = 0
        # use it to be able to reference offsets in min_coins
        for i in range(1, amount + 1):
            # print(i)
            for c in coins:
                # for amount i check all prior min coins for each difference between i and coin possible
                # add 1 to prior amount (due to taking up the amount of the current coin checking
                # then take the smallest amount based on every result (storing the min as we go)
                # due to default state of 0 if have an exact match,
                # we will automatically add 1 when comparing a coin = current amount i
                # so no need for separate ifs between > vs = 0
                if i - c >= 0:
                    # print(min_coins[i], min_coins[i - c] + 1)
                    min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)
        # print(min_coins)
        # check last amount in memoized data, if unchanged then no combination worked
        # otherwise the value is the minimum amount of coins
        if min_coins[-1] > amount:
            return -1
        return min_coins[-1]
                    


        
        
# @leet end
