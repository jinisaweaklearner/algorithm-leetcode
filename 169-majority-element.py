class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use hash map
        mapping = dict()
        # set up the max value for result
        max_value = 0 

        for v in nums:
            # update the mapping frequency
            mapping[v] = 1 + mapping.get(v, 0)

            # update the result if the frequency is larger than the max value
            if mapping[v] > max_value:
                result = v
            # every time update the max value
            max_value = max(max_value, mapping[v])
            # print(mapping, max_value)
        return result
        