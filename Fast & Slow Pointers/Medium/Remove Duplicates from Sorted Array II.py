# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # - Each unique number appears <= 2 times
        # - Sorted in increasing order

        # 2 pointers:
        # - insert_idx (Insertion pointer, where to swap the current element to here)
        #    - Also === "k"
        #    - Denotes the elements we WANT TO KEEP (everything LEFT <- is a swapped element)
        # - current_idx (Current element, swap this to the insertion pointer)
        # Swap the current_idx element to insert_idx if we want to keep it
        # Else, replace at next valid element

        # Pseudocode
        # Iterate the array:
            # current_num_count (occurence of current number)
            # If same number:
                # If >= 2:
                #   Limit reached, do not swap
                # else:
                #   insert_idx <-> current_idx
                #   insert_idx += 1
                # current_num_count += 1
            # Else
            #   current_num_count = 1 - Reset current num count, new number encountered
            # current_idx += 1
        
        insert_idx = 0
        current_tracked_num_count = 0
        current_tracked_num = nums[0]
        for current_idx in range(0, len(nums), 1):
            current_num = nums[current_idx]
            if current_num == current_tracked_num:
                current_tracked_num_count += 1

                # Still within limits, swap
                if current_tracked_num_count <= 2:
                    nums[insert_idx] = nums[current_idx]
                    insert_idx += 1
            else:
                # Number changed, reset the count!
                current_tracked_num = nums[current_idx]
                current_tracked_num_count = 1

                # Remember to swap
                nums[insert_idx] = nums[current_idx]
                insert_idx += 1
        
        return insert_idx


