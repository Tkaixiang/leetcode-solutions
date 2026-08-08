# https://leetcode.com/problems/4sum/
class Solution:
    # O(n^3)
    # Optimisation comes from twoSum() -> O(n)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]: # O(n)
        # 1. Iterate through
        # 2. Find triplet for (target - nums[x])
        nums.sort()

        starting_val_set = {}
        quadruplet_set = {}
        quadruplets = []
        for x in range(0, len(nums), 1):
            if nums[x] in starting_val_set: # Skip duplicate values of nums[x]
                continue
            
            starting_val_set[nums[x]] = 1
            # Find such that x (current num) + (-x)(triplet) === target
            result = self.threeSum(nums, target - nums[x], x+1)
            if len(result) == 0:
                continue
            
            for triplet in result:
                quadruplet = [nums[x], triplet[0], triplet[1], triplet[2]]

                # Check for duplicate quadruplets
                quadruplet_str = f"{nums[x]}_{triplet[0]}_{triplet[1]}_{triplet[2]}"
                if quadruplet_str in quadruplet_set:
                    continue
                
                quadruplet_set[quadruplet_str] = 1
                quadruplets.append(quadruplet)
        
        return quadruplets


    
    def threeSum(self, nums: list[int], target: int, start: int) -> list[list[int]]: # O(n)
        # 1. Not using the same element
        # 2. Triplets add to target

        # For each x:
        #   twoSum() and find me -x
        #   x + (-x) = 0

        triplets = []
        triplets_set = set()
        starting_val_set = {}
        for x in range(start, len(nums), 1):
            if nums[x] in starting_val_set: # Skip duplicate values of nums[x]
                continue
            
            starting_val_set[nums[x]] = 1

            # Find such that x (current num) + (-x)(pair) === target
            result = self.twoSum(target - nums[x], nums, x+1)
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

    # O(n)
    # Naive style: O(n^2)
    #   - Nested for loop iterate every possibility
    def twoSum(self, target, nums, start): 
        hash_table = {}
        pairs = []

        for x in range(start, len(nums)):
            sum_needed = target - nums[x]
            if sum_needed in hash_table:
                pairs.append([nums[x], sum_needed])
            
            hash_table[nums[x]] = 1
        return pairs