#LeetCode Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}  #it contains the value and the index

        for i, value in enumerate(nums):  #O(n)
            diff = target - nums[i]

            if diff in seen:             
                return [i,seen[diff]]
            else:
                seen[value] = i