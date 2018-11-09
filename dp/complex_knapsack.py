import numpy as np
from sys import maxsize

min_minus_int = -maxsize - 1


class MonoQueue:
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
                break
        else:
            tail += 1

        # head = min(head, tail - 1)
        self._cursors = (head, tail)

        self._array[tail - 1] = (value, index)

    def get(self) -> int:
        head, tail = self._cursors
        if head == tail:
            return 0

        value, index = self._array[head]
        index = index

        return value

    def reset(self, window: int):
        self._window = window
        self._cursors = (0, 0)

    def clear_old_value(self, index):
        head, tail = self._cursors
        for j in range(head, tail):
            v, i = self._array[j]
            if index - i > self._window:
                head += 1

        # head = min(head, tail - 1)
        self._cursors = (head, tail)


class Knapsack:
    def __init__(self, volume: int):
        self._weight = volume

    def wrap(self, v: tuple, w: tuple, m: tuple) -> np.ndarray:
        """
            : Same solution with complete knapsack. There are n single ones for i-th item, so we change it to 0-1 
            knapsack problem.
        """
        n = len(v)
        dp = np.zeros(self._weight + 1, dtype=np.int)
        
        for i in range(n):
            l = min(m[i], self._weight // w[i])
            for k in range(l):
                for W in range(self._weight, w[i] - 1, -1):
                    dp[W] = max(dp[W - w[i]] + v[i], dp[W])

        return dp

    def wrap_opt(self, v: tuple, w: tuple, m: tuple) -> np.ndarray:
        """
            : Same solution with complete knapsack. There are n single ones for i-th item, so we change it to 0-1 
            knapsack problem.
        """
        n = len(v)
        dp = np.zeros(self._weight + 1, dtype=np.int)
        
        for i in range(n):
            k = 1
            l = min(m[i], self._weight // w[i])
            while l > 0:
                for W in range(self._weight, w[i] * k - 1, -1):
                    dp[W] = max(dp[W - w[i] * k] + v[i] * k, dp[W])
                l -= k
                k = min(2 * k, l)

        return dp

    def wrap_opt_exact_match(self, v: tuple, w: tuple, m: tuple) -> np.ndarray:
        """
            : Same solution with complete knapsack. There are n single ones for i-th item, so we change it to 0-1 
            knapsack problem.
        """
        n = len(v)
        dp = np.array([-1] * (self._weight + 1), dtype=np.int)
        
        for i in range(n):
            k = 1
            l = min(m[i], self._weight // w[i])
            while l > 0:
                for W in range(self._weight, w[i] * k - 1, -1):
                    if W == w[i] * k:
                        dp[W] = v[i] * k
                    elif dp[W - w[i] * k] != -1:
                        dp[W] = max(dp[W - w[i] * k] + v[i] * k, dp[W])
                l -= k
                k = min(2 * k, l)

        return dp

    def wrap_optimum(self, v: tuple, w: tuple, m: tuple) -> np.ndarray:
        """
            : MonoArray, when the index value of a node is less than k
            the node is removed from the MonoQueue
        """
        n = len(v)
        dp = np.zeros(self._weight + 1, dtype=np.int)
        mq = MonoQueue(self._weight + 1)
        
        for i in range(n):
            cnt = min(self._weight // w[i], m[i])
            for r in range(w[i]):
                mq.reset(cnt)
                for W in range(r, self._weight + 1, w[i]):
                    k = W // w[i]
                    mq.put(dp[W] - k * v[i], k)
                    dp[W] = mq.get() + k * v[i]

        return dp


    def wrap_optimum_exact_match(self, v: tuple, w: tuple, m: tuple) -> np.ndarray:
        n = len(v)
        dp = [0] + [None] * self._weight
        mq = MonoQueue(self._weight + 1)
        
        for i in range(n):
            cnt = min(self._weight // w[i], m[i])
            for r in range(w[i]):
                if dp[r] is None:
                    continue

                mq.reset(cnt)
                for W in range(r, self._weight + 1, w[i]):
                    k = W // w[i]

                    if dp[W] is None:
                        mq.clear_old_value(k)

                        if all(dp[W - j * w[i]] is None for j in range(min(k, cnt), 0, -1)):
                            continue
                    else:
                        mq.put(dp[W] - k * v[i], k)
    
                    dp[W] = mq.get() + k * v[i]

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
r7 = knapsack.wrap_optimum_exact_match((13, 3, 10, 5, 6), (5, 4, 7, 2, 6), (2, 3, 1, 3, 10))
print(r7)

print("\n8. wrap_opt_exact_match")
r8 = knapsack.wrap_opt_exact_match((12, 6, 10, 5, 2), (5, 3, 1, 2, 1), (1, 2, 1, 2, 2))
print(r8)
r8 = knapsack.wrap_optimum_exact_match((12, 6, 10, 5, 2), (5, 3, 1, 2, 1), (1, 2, 1, 2, 2))
print(r8)

print("\n9. wrap_opt_exact_match(Complete knapsack)")
r9 = knapsack.wrap_opt_exact_match((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 10, 10))
print(r9)
r9 = knapsack.wrap_optimum_exact_match((12, 3, 10, 5, 6), (5, 4, 7, 2, 6), (10, 10, 10, 10, 10))
print(r9)

pass
