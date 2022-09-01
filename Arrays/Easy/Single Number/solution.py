class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for x in nums:
            if (x in hashMap):
                hashMap[x] += 1
            else:
                hashMap[x] = 1
        
        for x in hashMap:
            if (hashMap[x] == 1):
                return x