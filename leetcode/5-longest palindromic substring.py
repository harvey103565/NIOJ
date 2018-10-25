class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # r_border is the right border that have been explored
        r_border = 0
        # pivot is the center of palindromic substring defined by r_border
        pivot = 0
        # best pivot
        best_pivot = 0
        # longest length
        longest = 0

        dp = [1] * (2 * n + 1)

        # Change string to form [# a # b # a #], and we do not need to check # at head or tail
        for p in range(1, n * 2):
            if p < r_border:
                i = 2 * pivot - p
                dp[p] = min(dp[i], r_border - p + 1)
            else:
                dp[p] = 1 + p % 2
            
            for k in range(dp[p], min(p, 2 * n - p), 2):
                # k starts from 1 reasults that position p is ignored when p is odd(point at letters)
                if s[(p - k - 1) // 2] != s[(p + k) // 2]:
                    break
                dp[p] += 2
                # '#' is skipped when moving from 1 letter to another, saying that 2 positions is counted
            
            if dp[p] > longest:
                longest = dp[p]
                best_pivot = p

            r_explored = (p + dp[p] - 1)
            if r_border < r_explored:
                r_border = r_explored
                pivot = p

        return max(dp) - 1, s[(best_pivot + 1 - dp[best_pivot]) // 2: (best_pivot - 1 + dp[best_pivot]) // 2]
        # Why dp[x] - 1?  Consider that dp[5]('c') = 6 for string "# a # b # c # b # a #" there are n chars and n #s 
        # on the right side of 'c', which add up to 2n(6 in this case).
        # Both side total: 2(n chars + n #s) - 2n #s = 2n chars, however 'c' has been counted twice. 
        # So total chars: 2n - 1 which is dp[x] - 1
        # For dp[4], the symbol at x is '#' when x is even. To each side of '#' there are n chars and n '#'(exclude itself)
        # So we should only remove '#' at position x, then the result is dp[x] - 1 as well.

            
s = Solution()

r0 = s.longestPalindrome("")
print(r0)

r1 = s.longestPalindrome("aa")
print(r1)

r2 = s.longestPalindrome("aba")
print(r2)

r3 = s.longestPalindrome("abba")
print(r3)

r4 = s.longestPalindrome("abab")
print(r4)

r5 = s.longestPalindrome("ababa")
print(r5)

r6 = s.longestPalindrome("ababbab")
print(r6)

r7 = s.longestPalindrome("aaaa")
print(r7)

pass

