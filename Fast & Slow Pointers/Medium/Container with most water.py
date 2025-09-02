class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. Widest x-length
        # 2. Largest smaller block (i.e the y length is maximised, but we always take the smallest block else it will overflow)

        left = 0
        right = len(height) - 1
        # Guarunteed n >= 2
        # 1. We start at the LARGEST X-LENGTH possible

        maxWater = 0

        while left < right:
            lowerHeight = None
            if height[left] < height[right]:
                lowerHeight = height[left]
            else:
                lowerHeight = height[right]

            xDistance = right - left
            water = lowerHeight * xDistance  # Height * x-distance
            if water > maxWater:
                maxWater = water

            # 2. Afterwards, we try to optimise for the "highest height"
            # If left is the lower height, we increment it to find a new height
            # If right is the lower height, we decrement it to find a new height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater
