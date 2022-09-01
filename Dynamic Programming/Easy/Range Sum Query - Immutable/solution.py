class NumArray:

    def __init__(self, nums: List[int]):
        self.preSumArray = nums 
        for x in range(1, len(nums), 1):
            self.preSumArray[x] += self.preSumArray[x-1]
        
        # ===== PRESUM =====
        # [a,b,c,d,e] <-- Original
        # [a, a+b, a+b+c, a+b+c+d, a+b+c+d+e] <-- Each value is the sum of the previous value + current value
        
        # The sum of [1,3] is b+c+d == (a+b+c+d)-(a) == Element 3 - Element 0
        # If [0, 3], it is simply a+b+c+d, so just return the right indice, [3]
        

    def sumRange(self, left: int, right: int) -> int:
        if (left == 0): return self.preSumArray[right]
        else: return self.preSumArray[right] - self.preSumArray[left-1]
        
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)