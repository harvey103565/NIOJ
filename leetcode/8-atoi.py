INT_MAX = 0x7FFFFFFF
INT_MIN = -INT_MAX - 1
np = INT_MAX // 10
mp = INT_MAX % 10 + 1

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = 0
        fc = 1

        for i, c in enumerate(str.strip()):
            if i == 0 and c in ['-', '+']:
                if c == '-':
                    fc = -1
            else:
                if c.isdigit():
                    n = int(c)
                    if (num > np or (num == np and ((n >= mp and fc > 0) or (n > mp and fc < 0)))):
                        return INT_MAX if fc > 0 else INT_MIN
                    num = num * 10 + n
                else:
                    break
        return num * fc


s = Solution()

r = s.myAtoi("-42")
print(r)

r = s.myAtoi(" +11")
print(r)

r = s.myAtoi("-121A")
print(r)

r = s.myAtoi("A10")
print(r)

r = s.myAtoi("0-5")
print(r)

r = s.myAtoi("-5-")
print(r)

r = s.myAtoi("+-0")
print(r)

r = s.myAtoi("-137848731137848731137848731137848731")
print(r)

r = s.myAtoi("A210B")
print(r)

r = s.myAtoi("137848731137848731137848731137848731")
print(r)

pass

