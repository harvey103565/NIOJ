import numpy as np

class Knapsack:
    def __init__(self, volumn: int):
        self._volumn = volumn

    def wrap(self, value: list, cost: list) -> list:
        """
        Wrap all item into knapsack
            : For complete knapsack problem, every item could be taken as many times as it could be. It's ordinary 
            way to treat such item as a set of sigal ones. Then add them into sack one by one. This turns complete 
            knapsack problem into zero one subtype. Since quantity of each items is actually infinite, so we must use 
            volume / cost to determine how many times it could be add. 
            Be noticed that, the dp matrix is extended as items are splitted. However, if we use optimzed method in
            zero one problem, any one demension matrix with the size of v is required. Thus, this is the way.

        """
        n = len(value)
        dp = np.zeros(self._volumn + 1, dtype=np.int)
        
        for i in range(n):
            k = self._volumn // cost[i]
            for l in range(k):
                for j in range(self._volumn, cost[i] - 1, -1):
                    dp[j] = max(dp[j - cost[i]] + value[i], dp[j])

        return dp

    def wrap_opt(self, value: list, cost: list) -> list:
        """
        Wrap all item into knapsack
            : A small optimization. Items are divided following the rule: [1/2, 1/4, 1/8, ... ] rather than [1, 1, 1]
            So the middle loop(the k-loop) run log(n) times instead of n time.

        """
        n = len(value)
        dp = np.zeros(self._volumn + 1, dtype=np.int)
        
        for i in range(n):
            k = 1
            l = self._volumn // cost[i]
            while k <= l:
                for j in range(self._volumn, cost[i] * k - 1, -1):
                    dp[j] = max(dp[j - cost[i] * k] + value[i] * k, dp[j])
                k *= 2

        return dp


knapsack = Knapsack(14)

# r1 = knapsack.wrap((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
# print(r1)

r2 = knapsack.wrap((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r2)

r3 = knapsack.wrap_opt((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r3)

pass
