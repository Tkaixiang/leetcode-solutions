class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Merge Sort (a single merge)
        # 1. Make a copy of the mergable portion of nums1 as nums1_copy[int]
        # 2. Iterate both arrays
        # 3. If nums1_copy[i] < nums2[j]
        #  - Set nums1[idx]=nums1_copy[i]
        #  - Advance i
        # Else
        #  - Set nums1[idx]=nums2[j]
        #  - Advance j 

        nums1_copy = nums1[:m]
        total_elements = m + len(nums2)

        nums1_ptr = 0
        nums2_ptr = 0
        idx = 0
        while (idx < total_elements and nums1_ptr < len(nums1_copy) and nums2_ptr < len(nums2)):
            current_nums1 = nums1_copy[nums1_ptr]
            current_nums2 = nums2[nums2_ptr]
            if (current_nums1 < current_nums2):
                nums1[idx] = current_nums1
                nums1_ptr += 1
            else:
                nums1[idx] = current_nums2
                nums2_ptr += 1
            
            idx += 1

        # NOTE: Only 1 of these will run (since 1 will be empty)
        # Append any remaining nums1
        for x in range(nums1_ptr, len(nums1_copy)):
            nums1[idx] = nums1_copy[x]
            idx += 1
        
        # Append any remaining nums2
        for x in range(nums2_ptr, len(nums2)):
            nums1[idx] = nums2[x]
            idx += 1