# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Sliding Window
        # - Window can have <= 1 (zeroes)
        # - If Reached end without any windows shrinking
        #   - need to do 1 final check


        # left = 0
        # right = 0
        # - If num_zeros > 1:
        #  Get window length, see if longest
        #  Set left = previous_zero + 1 (exclude the previous zero)

        # End check:
        # length = right-left+1 - 1 = right - left (always need to remove 1 element)

        left = 0
        right = 0
        num_zeroes = 0
        position_last_zero = -1

        longest_size = 0
        while (right < len(nums)):
            current = nums[right]
            if current == 0:
                if num_zeroes == 1: # num_zeros is either 0 or 1
                    # Exceeded 0s allowed!
                    # Check size, then shrink window
                    length = (right-1)-left # -1 since we want to calc until BEFORE we exeeded our zeros quota
                    if length > longest_size:
                        longest_size = length
                    left = position_last_zero + 1
                    # No need to reset 0s count since we just met another 0:
                    # nums_zero = 0
                    # nums_zero = 1
                else:
                    num_zeroes = 1
                position_last_zero = right
            right += 1

        # 1 Last check
        # Reached end without any windows shrinking
        length = (right-1)-left
        if length > longest_size:
            longest_size = length
        
        return longest_size

                
                