# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a "Sliding Window" substring
        # When a matching char is reached, remove all chars that are <= previous char

        # Example: bacabc
        # - Matching char found at pos 3 (a), exclude all chars <= the previous matching char a (pos 1)
        #   - Effectively, shrinking the "sliding window" by moving the left pointer to pos 2 (c)

        longest_length = 0
        left = 0
        right = 0
        current_chars = {}

        for i, aChar in enumerate(s):
            if aChar in current_chars and current_chars[aChar] != -1:
                duplicate_char_index = current_chars[aChar]
                left = duplicate_char_index + 1
                for dupChar in current_chars:
                    if current_chars[dupChar] <= duplicate_char_index:
                        current_chars[dupChar] = -1

            current_chars[aChar] = i
            right = i

            length = right - left + 1
            if length > longest_length:
                longest_length = length

        return longest_length
