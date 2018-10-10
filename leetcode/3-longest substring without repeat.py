class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_longest_start = -1
        chr_reg = dict()    # last position that the character was found
        result = 0
        for i, c in enumerate(s):
            if c in chr_reg:
                prev_pos = chr_reg[c]
                if last_longest_start < prev_pos:
                    the_substring_length = i - prev_pos
                    prev_substring_length = i - 1 - last_longest_start
                    result = max(result, the_substring_length, prev_substring_length)
                    last_longest_start = prev_pos
                else:
                    prev_substring_length = i - 1 - last_longest_start
                    result = max(result, prev_substring_length)
                    

            chr_reg[c] = i

        else:
            if s:
                rest_substring_length = i - last_longest_start
                result = max(result, rest_substring_length)
                
        return result


solu = Solution()

result = solu.lengthOfLongestSubstring(' ')

