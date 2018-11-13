class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {')': '(', ']': '[', '}': '{'}
        n = len(s)
        i = -1
        stack = [''] * n

        for ch in s:
            if ch in parentheses:
                if i < 0 or stack[i] != parentheses[ch]:
                    return False
                else:
                    i -= 1
            else:
                i += 1
                stack[i] = ch

        return i == -1


s = Solution()

r = s.isValid(r'')
print(r)

r = s.isValid(r']')
print(r)

r = s.isValid(r'()')
print(r)

r = s.isValid(r'([)]')
print(r)

r = s.isValid(r'()[]{}')
print(r)

r = s.isValid(r'([]')
print(r)

r = s.isValid(r'(])')
print(r)
