# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            current_sum = numbers[left] + numbers[right]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                break

        return [left + 1, right + 1]
