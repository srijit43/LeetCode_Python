#Find minimum in a rotated sorted array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]   #declare as leftmost
        l , r = 0 , len(nums) - 1  #declare your left and right pointers

        while l<=r:  #always needs to be valid
            if nums[l] < nums[r]:
                res = min(res, nums[l])   #check the initial
                break
            
            m = (l + r)//2   #define pivot
            res = min(res, nums[m])
            if nums[m] >= nums[l]:  #basic binary search technique
                l = m + 1
            else:
                r = m - 1
        return res

