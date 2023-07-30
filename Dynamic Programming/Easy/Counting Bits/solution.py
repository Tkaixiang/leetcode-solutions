# https://leetcode.com/problems/counting-bits/
class Solution:
    def countBits(self, n: int) -> List[int]:
        outputArray = []
        
        # memorisation to speed things up for numbers we already calculated before
        memorisation = {}
        for i in range(0, n+1, 1):
            counter = i
            ones = 0
            while (counter > 0):
                if (counter in memorisation):
                    # reached a number we calculated before
                    # can just add the memorised ones and set to 0
                    ones += memorisation[counter]
                    counter = 0 
                else:
                    remainder = counter % 2
                    if (remainder == 1):
                        ones += 1
                    counter = counter // 2
            
            memorisation[i] = ones
            outputArray.append(ones)
        
        return outputArray
                