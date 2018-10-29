class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        m = 0
        n = x
        while n > 0:
            m = m * 10 + n % 10
            n = n // 10

        return x == m


s = Solution()

r = s.isPalindrome(1)
print(r)

r = s.isPalindrome(11)
print(r)

r = s.isPalindrome(121)
print(r)

r = s.isPalindrome(10)
print(r)

r = s.isPalindrome(100)
print(r)

r = s.isPalindrome(1010)
print(r)

r = s.isPalindrome(1100)
print(r)

r = s.isPalindrome(-121)
print(r)

r = s.isPalindrome(137848731)
print(r)

pass

    