class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        num_mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if not digits:
            return []

        def gen(digits):
            if len(digits) > 1:
                for c in num_mapping[digits[0]]:
                    for s in gen(digits[1:]):
                        yield c + s
            else:
                for c in num_mapping[digits[0]]:
                    yield c

        return [s for s in gen(digits)]

s = Solution()

r = s.letterCombinations('23')
print(r)

pass
