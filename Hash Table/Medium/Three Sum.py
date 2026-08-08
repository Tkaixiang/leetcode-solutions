# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1. Not using the same element
        # 2. Triplets add to 0

        # For each x:
        #   twoSum() and find me -x
        #   x + (-x) = 0

        nums.sort()

        triplets = []
        triplets_set = set()
        starting_val_set = {}
        for x in range(0, len(nums), 1):
            if nums[x] in starting_val_set: # Skip duplicate values of nums[x]
                continue
            
            starting_val_set[nums[x]] = 1

            # Find such that x (current num) + (-x)(pair) === 0
            result = self.twoSum(-nums[x], nums, x+1)
            if len(result) == 0:
                continue
            
            for pair in result:
                triplet = [nums[x], pair[0], pair[1]]
                # Check for duplicate triplets
                # [-1,1,0] === [0,1,-1] in this case
                triplet_str = f"{nums[x]}_{pair[0]}_{pair[1]}"
                if triplet_str in triplets_set:
                    continue

                triplets_set.add(triplet_str)
                triplets.append(triplet)
        
        return triplets
            

    # skip = current used element, can't use again
    # Returns -> ALL pairs that fit target
    def twoSum(self, target, nums, start):
        hash_table = {}
        pairs = []

        for x in range(start, len(nums)):
            sum_needed = target - nums[x]
            if sum_needed in hash_table:
                pairs.append([nums[x], sum_needed])
            
            hash_table[nums[x]] = 1
        return pairs
