# https://leetcode.com/problems/3sum/description/
class Solution:
    def twoSumAllPairs(self, nums, start_index, target):
        valid_pairs = []
        left = start_index
        right = len(nums) - 1
        while left < right:
            total_sum = nums[left] + nums[right]
            if total_sum == target:
                valid_pairs.append([nums[left], nums[right]])
                # Restrict both ways from here since we do not want the same result again
                left += 1
                right -= 1
            elif total_sum < target:
                # Too small, we need bigger number!
                left += 1
            else:
                right -= 1

        return valid_pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left = 0
        right = len(nums) - 1

        triplets = []
        triplet_hashes = {}
        nums.sort()

        # Idea: If we are to FIX one number, it essentially becomes a two-sum problem!
        for x in range(0, len(nums), 1):
            fixed_number = nums[x]
            target_to_find = -fixed_number
            two_index_pairs = self.twoSumAllPairs(nums, x + 1, target_to_find)

            for pair in two_index_pairs:
                triplet_hash = f"{fixed_number}_{pair[0]}_{pair[1]}"
                if triplet_hash not in triplet_hashes:
                    triplet_hashes[triplet_hash] = 1
                    triplets.append([fixed_number, pair[0], pair[1]])

        return triplets
