import numpy as np

class MonotonicArray:
    def __init__(self, values: np.ndarray):
        self._values = values
        self._capacity = len(values)
        self._array = np.zeros(self._capacity)
        self._cnt = 0
        self._head = 0
        self._tail = 0

    def add(self, index: int):
        for i in range(-1, -self._cnt - 1, -1):
            if self._values[index] < self._values[self._array[i]]:
                

class Knapsack:
    def __init__(self, volume: int):
        self._volume = volume

    def wrap(self, value: tuple, size: tuple, quantity: tuple) -> np.ndarray:
        """
            : Same solution with complete knapsack. There are n single ones for i-th item, so we change it to 0-1 
            knapsack problem.
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros(self._volume + 1, dtype=np.int)
        
        for i in range(n):
            k = min(quantity[i], self._volume // size[i])
            for l in range(k):
                l = l   # eliminate warning
                for v in range(self._volume, size[i] - 1, -1):
                    dp[v] = max(dp[v - size[i]] + value[i], dp[v])

        return dp

    @staticmethod
    def monotone_add(k: int, n: int, l: list, v: tuple) -> int:
        for i in range(-1, -n - 1, -1):
            if v[l[i]] >= v[k]:         # if current element in queue is larger than given value(k), 
                break                   # then stop seek backwardly
        n = n + i + 1                   # n(n=len(l)) + i is current element(i starts from -1)
        l[n] = k                        # l[n + i + 1] is next value(new tail, the minimum)
        return n

    def wrap_optimum(self, value: tuple, size: tuple, quantity: tuple) -> np.ndarray:
        """
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros(self._volume + 1, dtype=np.int)
        mq = np.zeros(self._volume)
        for i in range(n):
            pass

        return dp
            

knapsack = Knapsack(15)

r1 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (1, 1, 1, 1, 1))
print(r1)


pass
