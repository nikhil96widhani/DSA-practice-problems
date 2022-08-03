class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1

        return nums1


if __name__ == '__main__':
    sol = Solution()
    ans = sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(ans)
