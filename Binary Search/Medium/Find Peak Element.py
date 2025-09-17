# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lower = 0
        higher = len(nums) - 1
        while lower <= higher:
            mid = int((lower + higher) / 2)
            element = nums[mid]
            if (mid - 1 < 0 or nums[mid - 1] < element) and (
                mid + 1 > len(nums) - 1 or nums[mid + 1] < element
            ):
                # We found a peak element!
                return mid
            elif mid - 1 >= 0 and nums[mid - 1] > element:
                higher = mid - 1
                # The leftside slops upwards, let's follow it to hopefully a peak!
            else:
                lower = mid + 1
