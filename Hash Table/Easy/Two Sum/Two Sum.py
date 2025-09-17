# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if num in hash_table:
                hash_table[num].append(i)
            else:
                hash_table[num] = [i]

        for num in hash_table:
            difference = target - num
            current_index = hash_table[num][0]

            if difference in hash_table:
                # Possible difference found
                num_list = hash_table[difference]
                for index_in_difference in num_list:
                    if (
                        index_in_difference == current_index
                    ):  # Do not use the same index number
                        continue

                    return [current_index, index_in_difference]
