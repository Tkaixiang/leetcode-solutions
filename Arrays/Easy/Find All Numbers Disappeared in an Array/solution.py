class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missingNumbers = []
        numsHashMap = {}
        for x in nums:
            numsHashMap[x] = 0
        
        for x in range(1, len(nums)+1, 1):
            if (x not in numsHashMap):
                missingNumbers.append(x)

        return missingNumbers
        