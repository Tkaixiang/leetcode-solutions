class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a "Sliding Window" substring
        # When a matching char is reached, remove all chars that are <= previous char
        
        # Example: dvedf
        # - Matching char found at pos 3, remove pos <= 0 char
        # - Optimisation: There is no need to "jump" back since we already checked all the characters until pos+1. So just remove everything LEFT of the sliding window
       
        currentSubString = ""
        largest = 0
        for x in s:
            
            lastPos = currentSubString.find(x)
            if (lastPos != -1):
                currentSubString += x
                currentSubString = currentSubString[lastPos+1:]
            else:
                currentSubString += x
            
            currentLen = len(currentSubString)
            if (currentLen > largest):
                largest = currentLen
        
        return largest
            
        