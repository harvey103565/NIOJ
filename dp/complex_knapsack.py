import numpy as np


class MonotoneArray:
    def __init__(self: int, col: int, window: int):
        self._array = np.zeros(col, dtype=np.int)
        self._cursors = (0, 0)
        self._window = window

    def put(self, value: int, index: int):
        head, tail = self._cursors

        for k in range(tail, head - 1, -1):
            v, i = self._array[k]
            if v > value:
                break
            tail = k
        self._array[tail] = (value, index)    

        for k in range(head, tail):
            v, i = self._array[k]
            if index - i < self._window:
                break
            head = k
            
        
        self._cursors = (head, tail)

    def get(self) -> int:
        head, tail = self._cursors
        value, index = self._array[head]
        return value

    def reset(self, window: int):
        self._window = window
        self._cursors = (0, 0)



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
            for j in range(size[i]):
                for k in range(c + 1):
                    queue.put(j, dp[], k)
                    pass

        return dp

            

knapsack = Knapsack(15)

r1 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (1, 1, 1, 1, 1))
print(r1)
r1 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (1, 1, 1, 1, 1))
print(r1)

r2 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 10, 10))
print(r2)
r2 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 10, 10))
print(r2)

r3 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 3, 10))
print(r3)
r3 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 3, 10))
print(r3)

r4 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 10, 10, 3, 10))
print(r4)
r4 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 10, 10, 3, 10))
print(r4)

r5 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 10, 10, 3, 10))
print(r5)
r5 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 10, 10, 3, 10))
print(r5)

r6 = knapsack.wrap((12, 6, 10, 5, 2), (5, 3, 1, 2, 1), (1, 2, 1, 2, 2))
print(r6)
r6 = knapsack.wrap_optimum((12, 6, 10, 5, 2), (5, 3, 1, 2, 1), (1, 2, 1, 2, 2))
print(r6)

pass
