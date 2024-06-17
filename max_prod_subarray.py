#Max product of sub array
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #always initate at max of the array
        curMax, curMin = 1,1 #1 is like a reset

        for n in nums:
            if n == 0:
                curMax, curMin = 1,1
                continue
            temp = curMax  #I want to keep my curMax intact before transformation
            curMax = max(n*curMax, n*curMin, n)  #n is new new number
            curMin = min(n*temp,n*curMin, n)
            res = max(curMax,res)
        return res