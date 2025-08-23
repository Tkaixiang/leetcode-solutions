class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimalLength = 0
        rollingSum = 0

        left = 0
        right = 0

        while right < len(nums):
            currentNum = nums[right]
            rollingSum += currentNum
            
            if (rollingSum >= target):
                # Try to shorten
                while (rollingSum - nums[left] >= target and left <= right):
                    rollingSum -= nums[left]
                    left += 1
                
                lengthOfWindow = right - left + 1
                if (minimalLength == 0 or lengthOfWindow < minimalLength):
                    minimalLength = lengthOfWindow

            right += 1
        
        return minimalLength