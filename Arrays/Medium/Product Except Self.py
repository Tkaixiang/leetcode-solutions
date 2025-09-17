# https://leetcode.com/problems/product-of-array-except-self/submissions/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Array: [1,2,3,4]
        # Prefix Product 1,2,6,24
        # Say I want to exclude 3, then it is (1 x 2) x 4
        # We need to store the products of the left and right for each index
        # E.g for 2, we need to store 1 (left-array) and 3 x 4 (right-array)
        left_array = [1] * len(nums)
        right_array = [1] * len(nums)

        product_so_far = 1
        # For each index i, stores the product of its entire left-side nums[:i]
        for x in range(0, len(nums), 1):
            left_array[x] = product_so_far
            product_so_far *= nums[x]

        product_so_far = 1
        # For each index i, stores the product of its entire right-side nums[i+1:]
        for x in range(len(nums) - 1, -1, -1):
            right_array[x] = product_so_far
            product_so_far *= nums[x]

        output = [1] * len(nums)
        # Finally, iterate through 1 last time to get the output
        for x in range(0, len(nums), 1):
            output[x] = left_array[x] * right_array[x]

        return output
