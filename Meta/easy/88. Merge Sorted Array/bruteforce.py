# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """

#         while len(nums2[0:n])>0:
#             for i, val in enumerate(nums1):
#                 if val>=nums2[0]:
#                     nums1.insert(i, nums2[0])
#                     nums2.pop(0)
#                     nums1.pop(-1)
#                     break
#                 elif i==m+n-len(nums2):
#                     nums1.insert(i, nums2[0])
#                     nums2.pop(0)
#                     nums1.pop(-1)
#                     break

#         return nums1

##### APPROACH 2 little bit faster
# KEEPING RECORD OF LAST INDEX CHANGED TO MAKE LOOP FASTER
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         lastinsert_index = None
#         while len(nums2[0:n]) > 0:
#             for i, val in enumerate(nums1):
#                 if lastinsert_index is None or i > lastinsert_index :
#                     if val >= nums2[0]:
#                         nums1.insert(i, nums2[0])
#                         nums2.pop(0)
#                         nums1.pop(-1)
#                         lastinsert_index = i+1
#                         break
#                     elif i == m + n - len(nums2):
#                         nums1.insert(i, nums2[0])
#                         nums2.pop(0)
#                         nums1.pop(-1)
#                         break
#
#         return nums1

# combining if and elseif
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        lastinsert_index = 0
        while n > 0:
            for i in range(lastinsert_index, len(nums1)):
                if nums1[i] >= nums2[0] or i == m + n - len(nums2):
                    nums1.insert(i, nums2[0])
                    nums2.pop(0)
                    nums1.pop(-1)
                    n -= 1
                    lastinsert_index = i + 1
                    break

        return nums1


if __name__ == '__main__':
    sol = Solution()
    ans = sol.merge([2, 0], 1, [1], 1)

    print(ans)
