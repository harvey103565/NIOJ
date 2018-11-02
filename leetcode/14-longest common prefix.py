class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        r = ''
        n = min((len(s) for s in strs))

        for i in range(n):
            ch = strs[0][i]
            chv = ord(ch)
            if any((ord(s[i]) - chv for s in strs[1:])):
                break

            r += ch

        return r


s = Solution()

r = s.longestCommonPrefix(["flower","flow","flight"])
print(r)

r = s.longestCommonPrefix(["dog","racecar","car"])
print(r)

pass