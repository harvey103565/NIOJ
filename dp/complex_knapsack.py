import numpy as np


class MonotoneArray:
    def __init__(self, row: int, col: int, window: int):
        self._array = np.zeros((row, col), dtype=np.int)
        self._coursors = [(0, 0)] * row
        self._window = window

    def put(self, row: int, value: int, index: int):
        head, tail = self._coursors[row]

        for k in range(tail, head - 1, -1):
            v, i = self._array[row][k]
            if v > value:
                self._array[row][k + 1] = (value, index)
                tail = k + 1
            if index - i >= self._window:
                head = k + 1
                break
        self._coursors[row] = (head, tail)


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

    def wrap_optimum(self, value: tuple, size: tuple, quantity: tuple) -> np.ndarray:
        """
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros(self._volume + 1, dtype=np.int)

        for i in range(n):
            c = min(self._volume // size[i], quantity[i])
            queue = MonotoneArray(size[i], self._volume, c)
            for k in range(c + 1):
                for j in range(size[i]):
                    pass

        return dp

            

knapsack = Knapsack(15)

r1 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (1, 1, 1, 1, 1))
print(r1)


pass
