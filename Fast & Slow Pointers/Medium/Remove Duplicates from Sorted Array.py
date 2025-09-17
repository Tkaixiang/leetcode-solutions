# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        # We operate on n >= 2 arrays only
        # Our left is the "baseline" number to compare with
        # Our right is the "current" number we are comparing with
        # E.g in [1,1,1,2,2,3], left = 1 (index 0), right = 1 (index 1) for example
        baseline = 0
        current = 1

        number_of_current_num = 1
        while current < len(nums):
            if nums[baseline] == nums[current]:
                # Our aim here is to keep "baseline" at the right-most edge of the same numbers
                #    - This is to allow insertion into baseline + 1
                # E.g in [1,1,2,2,3], our "baseline" should be at index 1 eventually
                if number_of_current_num == 1:
                    # We want to keep this "current" number, baseline + 1 and move current to here
                    baseline += 1
                    nums[baseline] = nums[current]

                # Duplicate detected, don't keep
                # Will be replaced by the next "different number" (see below)
                number_of_current_num += 1

            else:
                # "current" number is different
                # We need to write the new number into "baseline" + 1
                number_of_current_num = 1
                baseline += 1  # Set baseline to the current num since it is different
                nums[baseline] = nums[current]

            current += 1

        return baseline + 1
