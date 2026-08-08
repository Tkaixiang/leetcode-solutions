# https://leetcode.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 3Sum -> Find all triplets that sum to 0
        # 3Sum Closest -> Find A triplet whose sum is closest to target

        # 1. Iterate through nums, pick X as starting num
        # 2. twoSum() modified: Find CLOSEST (target - X)
        # E.g Target = 1
        #    - Pick -1
        #    - abs(target - x) = 1 - (-1) = 2 [ABSOLUTE]
        #    - Find CLOSEST pair sums up to 2
        # 3. Variant to use:
        #  Hash table ❌, exact only
        #  2 Pointers ✅
        #    Left=x, Right=len(nums)-1
        #    <target -> Left += 1
        #    >target -> Right -= 1
        #    - Record SMALLEST difference to target
        #    - Record sum
        # 4. Return sum of pair (that resulted in smallest difference)
        # 5. Add current nums[x], does it beat smallest difference?

        nums.sort()

        seen_numbers = {}
        smallest_difference_triplet = 99999999999999999999999
        closest_triplet_sum = None
        for x in range(0, len(nums)-2, 1):

            # handles repeated nums such as [0,0,0]
            if nums[x] in seen_numbers:
                continue
            seen_numbers[nums[x]] = 1

            # target - nums[x]
            targetDifference = target - nums[x]
            # twoSum() modified
            #print("targetDifference", targetDifference)
            smallestTwoSumDifference = self.twoSumDifference(nums, targetDifference, x+1)
            #print("smalletTwoSumDifference", smallestTwoSumDifference)
            triplet = nums[x] + smallestTwoSumDifference

            # current difference
            current_difference = abs(target - triplet)
            #print("current triplet: ", [nums[x], smallestTwoSumDifference])
            if (current_difference < smallest_difference_triplet):
               
                smallest_difference_triplet = current_difference
                closest_triplet_sum = triplet
        
        return closest_triplet_sum
    
    # Returns a pair which is CLOSEST to target
    def twoSumDifference(self, nums, target, startNum):
        left = startNum
        right = len(nums) - 1

        smallestDifference = 99999999999999999999999
        sum_with_smallest_difference = None
        while (left < right):
            current_sum = nums[left] + nums[right]
            difference = abs(target - current_sum)
            if (difference < smallestDifference):
                smallestDifference = difference
                sum_with_smallest_difference = current_sum
            
            if (current_sum > target):
                right -= 1
            elif (current_sum < target):
                left += 1
            else:
                break # Exact found
        
        return sum_with_smallest_difference

            