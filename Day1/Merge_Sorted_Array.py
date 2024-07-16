class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of the arrays
        p1 = m - 1  # Pointer for nums1
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for the merged array (end of nums1)

        # While there are elements to compare in both arrays
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # No need to handle remaining elements in nums1
        # as they are already in their correct positions
