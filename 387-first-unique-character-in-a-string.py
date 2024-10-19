"""
Complexity:
Time Complexity: O(N), where N is the length of the input string.
Space Complexity: O(1) (constant space for the fixed-size list).
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        # get the first value
        for j in s:
            if count[j] == 1:
                return s.index(j)
        return -1