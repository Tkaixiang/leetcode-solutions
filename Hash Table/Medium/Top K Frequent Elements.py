# https://leetcode.com/problems/top-k-frequent-elements/submissions/1773619845/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        # Get frequency of each number
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        # Sort the numbers by their frequency
        nums_amount = []
        for num in hash_table:
            nums_amount.append((num, hash_table[num]))
        nums_amount.sort(key=lambda a: a[1], reverse=True)

        # Get the top k numbers
        output = []
        for x in range(0, k, 1):
            output.append(nums_amount[x][0])
        return output
