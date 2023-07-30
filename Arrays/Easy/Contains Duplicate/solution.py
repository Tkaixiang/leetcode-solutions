# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for x in nums:
            if (x in hashMap):
                return True
            hashMap[x] = 0
        
        return False