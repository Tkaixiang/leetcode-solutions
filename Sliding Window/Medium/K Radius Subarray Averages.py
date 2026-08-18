class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # k-radius average
        # o(nk) -> Up to "k" operations for EACH element in n-len array
        # We CANT run a full 2-sided sweep each element since that is 2k

        # Solution:
        # - At index i
        # - Take elements [nums[i-k]:nums[i+k]]
        # - Find average

        # [7] 4 3 >9< 1 8 [5] 2 6
        # [7] <-- left_edge pointer
        # [5] <-- right_edge pointer
        # Calculate Average: 
        #  - Sum = 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37
        #  - Average = 37 / 7 = 5
        #  - Clean up sum for next iteration: 37 - 7 = 30 [DROP nums[left_edge]]
        # 7 [4] 3 9 >1< 8 5 [2] 6
        #  - Sum = 30 + 2

        output = [-1 for x in range(len(nums))]

        if len(nums) > 2*k:
            left_edge = 0
            right_edge = 2*k
            current_sum = 0

            # Do the initial sum and the first k-radius average
            for x in range(0, right_edge+1, 1):
                current_sum += nums[x]
            output[k] = int(current_sum / (2*k + 1))

            # Start from k+1
            for centre_index in range(k+1, len(nums) - k):
                current_sum -= nums[left_edge]
                left_edge += 1
                right_edge += 1
                current_sum += nums[right_edge]

                output[centre_index] = int(current_sum / (2*k + 1))
        
        return output
