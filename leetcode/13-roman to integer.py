class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        ir_mapping = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        for i in range(len(s)):
            d = ir_mapping[s[i]]
            r = num % d
            if r:
                num = num + d - r * 2
            else:
                num = num + d

        return num


s = Solution()

r = s.romanToInt('XLIV')
print(r)

r = s.romanToInt('MCMXCIV')
print(r)

r = s.romanToInt('LVIII')
print(r)

r = s.romanToInt('IX')
print(r)

r = s.romanToInt('IV')
print(r)

r = s.romanToInt('IXIV')
print(r)

r = s.romanToInt('XCXL')
print(r)

r = s.romanToInt('CMCD')
print(r)

r = s.romanToInt('LIXIV')
print(r)

r = s.romanToInt('DXCXL')
print(r)

r = s.romanToInt('MCMCD')
print(r)

pass