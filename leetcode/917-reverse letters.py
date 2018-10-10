class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        def revertStr(S):
            cnt = len(S)
            for i in range(cnt):
                if 64 < ord(S[i]) < 91 or 96 < ord(S[i]):
                    yield (S[cnt - j - 1] for j in range(cnt))                    
                else:
                    yield S[i]

        a = list(revertStr(S))
    
        return a


s = Solution()
s.reverseOnlyLetters('Ab-Cd')