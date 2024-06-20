#Search in a sorted rotating array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1   #declare left and right pointer

        while l<=r:  #declare a holding condition
            m = (l+r)//2  #declare pivot

            if target == nums[m]:  #easy solution if pivot = target then done
                return m
            
            if nums[m]>=nums[l]:  # if pivot greater than left then pivot is part of left array
                if target > nums[m] or target < nums[l]:  #if target is bigger than pivot or less than left then we search right array
                    l = m + 1
                else:
                    r = m - 1

            else:
                if target < nums[m] or target > nums[r]:  #if target is lesser than pivot or greater than right then we search left array
                    r = m - 1
                else:
                    l = m + 1
        return -1


    
   