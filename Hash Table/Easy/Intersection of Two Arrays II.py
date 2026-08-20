# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_set = {}
        result = []

        # Create a num -> occurence set for nums2
        for num in nums2:
            if num in nums2_set:
                nums2_set[num] += 1
            else:
                nums2_set[num] = 1
        
        # Iterate nums1
        for num in nums1:
            if num in nums2_set:
                if nums2_set[num] == 1:
                    # Last occurence, remove it from set
                    del nums2_set[num]
                else:
                    nums2_set[num] -= 1
                
                result.append(num)
        
        return result

        