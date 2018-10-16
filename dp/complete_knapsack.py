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
        dp = np.zeros(self._volume + 1, dtype=np.int)
        
        for i in range(n):
            k = self._volumn // cost[i]
            for l in range(k):
                for j in range(self._volumn, cost[i] - 1, -1):
                    dp[j] = max(dp[j - cost[i]] + value[i], dp[j])

        return dp


knapsack = Knapsack(15)

r1 = knapsack.wrap((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
print(r1)

# r2 = knapsack.wrap_opt((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
print(r2)

pass
