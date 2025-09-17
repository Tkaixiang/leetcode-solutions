# https://leetcode.com/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest_sequence = 1
        numbers_present = (
            {}
        )  # Map numbers and to whether it has been counted "1: False"
        for x in nums:
            numbers_present[x] = False

        for num in numbers_present:
            if numbers_present[num] == True:
                continue  # Already counted

            current_sequence_length = 1

            upwards_search = num + 1
            # Search space upwards
            while (
                upwards_search in numbers_present
                and not numbers_present[upwards_search]
            ):
                numbers_present[upwards_search] = True
                current_sequence_length += 1
                upwards_search += 1

            downwards_search = num - 1
            # Search space downwards
            while (
                downwards_search in numbers_present
                and not numbers_present[downwards_search]
            ):
                numbers_present[downwards_search] = True
                current_sequence_length += 1
                downwards_search -= 1

            if current_sequence_length > longest_sequence:
                longest_sequence = current_sequence_length

        return longest_sequence
