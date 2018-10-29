class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        remainder = 0
        if 0 < x < 10:
            return True

        while x > 9:
            remainder = remainder * 10 + x % 10
            if x == remainder:
                return True

            x = int(x / 10)
            if x == remainder:
                return True
        
        return False


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

r = s.isPalindrome(-121)
print(r)

r = s.isPalindrome(137848731)
print(r)

pass

    