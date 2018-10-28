import numpy as np


class MonotoneArray:
    def __init__(self: int, col: int):
        self._array = [None] * col
        self._cursors = None
        self._window = 0

    def put(self, value: int, index: int):
        head, tail = self._cursors

        for j in range(head, tail):
            v, i = self._array[j]
            if index - i > self._window:
                head += 1
            
            if v < value:
                tail = j + 1
                head = min(head, tail - 1)
                break
        else:
            tail += 1

        self._array[tail - 1] = (value, index)
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
            l = min(quantity[i], self._volume // size[i])
            for k in range(l):
                for v in range(self._volume, size[i] - 1, -1):
                    dp[v] = max(dp[v - size[i]] + value[i], dp[v])

        return dp

    def wrap_opt(self, value: tuple, size: tuple, quantity: tuple) -> np.ndarray:
        """
            : Same solution with complete knapsack. There are n single ones for i-th item, so we change it to 0-1 
            knapsack problem.
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros(self._volume + 1, dtype=np.int)
        
        for i in range(n):
            k = 1
            l = min(quantity[i], self._volume // size[i])
            while l > 0:
                for v in range(self._volume, size[i] * k - 1, -1):
                    dp[v] = max(dp[v - size[i] * k] + value[i] * k, dp[v])
                l -= k
                k = min(2 * k, l)

        return dp

    def wrap_opt_exact_match(self, value: tuple, size: tuple, quantity: tuple) -> np.ndarray:
        """
            : Same solution with complete knapsack. There are n single ones for i-th item, so we change it to 0-1 
            knapsack problem.
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.array([-1] * (self._volume + 1), dtype=np.int)
        
        for i in range(n):
            k = 1
            l = min(quantity[i], self._volume // size[i])
            while l > 0:
                for v in range(self._volume, size[i] * k - 1, -1):
                    if v == size[i] * k:
                        dp[v] = value[i] * k
                    elif dp[v - size[i] * k] != -1:
                        dp[v] = max(dp[v - size[i] * k] + value[i] * k, dp[v])
                l -= k
                k = min(2 * k, l)

        return dp

    def wrap_optimum(self, value: tuple, size: tuple, quantity: tuple) -> np.ndarray:
        """
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros(self._volume + 1, dtype=np.int)
        ma = MonotoneArray(self._volume + 1)
        
        for i in range(n):
            cnt = min(self._volume // size[i], quantity[i])
            for r in range(size[i]):
                ma.reset(cnt)
                for v in range(r, self._volume + 1, size[i]):
                    k = v // size[i]
                    ma.put(dp[v] - k * value[i], k)
                    dp[v] = ma.get() + k * value[i]

        return dp

            

knapsack = Knapsack(15)

print("\n0. wrap vs warp_opt")
r0 = knapsack.wrap((13, 3, 10, 5, 6), (5, 4, 7, 2, 6), (1, 1, 1, 1, 1))
print(r0)
r0 = knapsack.wrap_opt((13, 3, 10, 5, 6), (5, 4, 7, 2, 6), (1, 1, 1, 1, 1))
print(r0)

print("\n1. wrap vs wrap_optimum")
r1 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (1, 1, 1, 1, 1))
print(r1)
r1 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (1, 1, 1, 1, 1))
print(r1)

print("\n2. wrap_opt vs wrap_optimum(Complete knapsack)")
r2 = knapsack.wrap_opt((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 10, 10))
print(r2)
r2 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 10, 10))
print(r2)

print("\n3. wrap_opt vs wrap_optimum")
r3 = knapsack.wrap_opt((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 3, 10))
print(r3)
r3 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 3, 10))
print(r3)

print("\n4. wrap_opt vs wrap_optimum")
r4 = knapsack.wrap_opt((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 10, 10, 3, 10))
print(r4)
r4 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 10, 10, 3, 10))
print(r4)

print("\n5. wrap_opt vs wrap_optimum")
r5 = knapsack.wrap_opt((13, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 10, 10, 3, 10))
print(r5)
r5 = knapsack.wrap_optimum((13, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 10, 10, 3, 10))
print(r5)

print("\n6. wrap_opt vs wrap_optimum")
r6 = knapsack.wrap_opt((12, 6, 10, 5, 2), (5, 3, 1, 2, 1), (1, 2, 1, 2, 2))
print(r6)
r6 = knapsack.wrap_optimum((12, 6, 10, 5, 2), (5, 3, 1, 2, 1), (1, 2, 1, 2, 2))
print(r6)

print("\n7. wrap_opt_exact_match")
r7 = knapsack.wrap_opt_exact_match((13, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 3, 1, 3, 10))
print(r7)

print("\n8. wrap_opt_exact_match")
r8 = knapsack.wrap_opt_exact_match((12, 6, 10, 5, 2), (5, 3, 1, 2, 1), (1, 2, 1, 2, 2))
print(r8)

print("\n9. wrap_opt_exact_match(Complete knapsack)")
r9 = knapsack.wrap_opt_exact_match((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 10, 10))
print(r9)

pass
