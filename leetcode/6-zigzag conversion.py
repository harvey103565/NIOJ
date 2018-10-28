class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        def zigChars(s, n, m):
            s1 = 2 * (m - 1)
            s2 = 0

            for i in range(m):
                k0 = i
                yield s[i]

                k1 = s1 - 2 * i
                k2 = s2 + 2 * i
                while k1 or k2:
                    if k1:
                        if k0 + k1 < n:
                            yield s[k0 + k1]
                        else:
                            break
    
                    if k2:
                        if k0 + k1 + k2 < n:
                            yield s[k0 + k1 + k2]
                        else:
                            break

                    k0 += (s1 + s2)
        n = len(s)
        if n <= numRows or numRows == 1:
            return s
        
        return ''.join(zigChars(s, n, numRows))


s = Solution()
r0 = s.convert("", 3)
print(r0)

r1 = s.convert("A", 1)
print(r1)

r2 = s.convert("AB", 1)
print(r2)

r3 = s.convert("PAYPALISHIRING", 3)
print(r3)

r4 = s.convert("PAYPALISHIRING", 4)
print(r4)

pass
