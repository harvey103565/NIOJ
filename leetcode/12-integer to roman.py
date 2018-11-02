class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        base_mapping = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        base = [1000, 500, 100, 50, 10, 5, 1]
        roman = ''
        n = len(base)
        for i, b in enumerate(base):
            result = num // b

            if result > 0:
                roman += base_mapping[b] * result

            num = num % b

            if num == 0:
                break

            m = b - base[i + 1]
            if num > m :
                roman += (base_mapping[base[i + 1]] + base_mapping[b])
                num -= m
        
        return roman

    def intToRoman_opt(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
        r = ''

        for b, s in base:
            r += s * (num // b)
            num = num % b
        
        return r



s = Solution()

r = s.intToRoman_opt(3)
print(r)

r = s.intToRoman(4)
print(r)

r = s.intToRoman(5)
print(r)

r = s.intToRoman_opt(9)
print(r)

r = s.intToRoman_opt(58)
print(r)

r = s.intToRoman_opt(1994)
print(r)

pass
