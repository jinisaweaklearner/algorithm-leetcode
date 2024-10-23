class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # as we have enough space in nums1, we can use it as a storage and make the comparison
        # setup the init pointer
        p1 = m -1
        p2 = n -1
        last = m +n -1

        # compare them when both pointers are >= 0
        while p2 >=0 and p1>=0 :
            if nums1[p1] >= nums2[p2]:
                nums1[last] =  nums1[p1]
                last -= 1
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[last] = nums2[p2]
                last -= 1
                p2 -= 1
        # update the remaining                 
        while p2 >= 0:
            nums1[last] = nums2[p2]
            last -= 1
            p2 -= 1


        return p1