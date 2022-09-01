import math

class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 4
        # 1+1...
        # 1+2+1
        # 2+1+1
        # 1+1+2
        # ^ The above can be reduced to 3 choose 1 (the position of 2), since the order of the "1s" don't matter
        # 2+2
        
        # n = 5
        # 1+1...
        # 2+2+1
        # 2+1+2
        # 1+2+2
        # 2+1+1+1
        
        # n = 6
        # 1+1...
        # 2+2+1+1
        # 2+1+2+1
        # 2+1+1+2
        # 1+2+1+2
        # 1+2+2+1
        # 1+1+2+2
        # ^ The above is 4 choose 2
        # 2+1+1+1+1
        # 2+2+2
        
        ways = 1
        numberOfTwos = n // 2
        for x in range(1, numberOfTwos+1, 1):
            numberOfOnes = n - (x*2) 
            sampleSize = numberOfOnes + x
            ways += int(math.factorial(sampleSize) / (math.factorial(x) * math.factorial(sampleSize - x)))
        
        return ways
            
        