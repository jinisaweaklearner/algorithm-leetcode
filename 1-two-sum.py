class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapping = dict()

        # store index and overwrite the index the large numer
        for i,v in enumerate(nums):
            mapping[v] = i

        # no need to sort as index can be changed

        for i in range(len(nums)):
            
            val = target - nums[i]
            
            # make sure the value we are looking for is in mapping
            if val in mapping and i != mapping[val]:
                return [i, mapping[val]]
