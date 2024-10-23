class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # remove duplicate
        result = set()

        # sort the array
        nums.sort()

        for i in range(len(nums)):
            # add two points
            left = i + 1
            right = len(nums) - 1

            # keep moving the left pointer less than right pointer
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0 :
                    right -= 1
                elif nums[i] + nums[left] + nums[right] == 0 :
                    result.add((nums[i] , nums[left], nums[right] ))
                    right -= 1
                    left += 1
                else:
                    left += 1
        
        return list(result)