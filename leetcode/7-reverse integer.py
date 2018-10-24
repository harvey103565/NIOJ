max_int = 0x7FFFFFFF
n1 = int(max_int / 10)
n2 = max_int % 10

min_int = -0x80000000
m1 = int(min_int / 10)
m2 = min_int % -10


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        b = 10 if x >= 0 else -10
        n = x
        while n:
            if (y > n1 or (y == n1 and n > n2) or y < m1 or (y == m1 and n < m2)):
                return 0
            y = y * 10 + n % b
            n = int(n / 10)
        
        return y

            
s = Solution()

r1 = s.reverse(13)
print(r1)

r2 = s.reverse(-4321)
print(r2)

r3 = s.reverse(7463847412)
print(r3)

r4 = s.reverse(1111111113)
print(r4)

r5 = s.reverse(-2147483648)
print(r5)

r6 = s.reverse(-8463847412)
print(r6)

pass
