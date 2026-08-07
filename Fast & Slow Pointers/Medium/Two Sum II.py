# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [2,4,5,7,11,15]
        # Target: 15
        # 2,15 = 17 > 15 [Right -= 1]
        # 2,11 = 13 < 15 [Left += 1]
        # 4,11 = 15 [Target found!]

        left = 0
        right = len(numbers) - 1
        while (True):
            add_numbers = numbers[left] + numbers[right]
            if (add_numbers == target):
                return [left+1, right+1]
            if (add_numbers > target):
                right -= 1
            elif (add_numbers < target):
                left += 1
