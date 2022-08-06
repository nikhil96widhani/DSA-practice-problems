class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # SORT FIRST AND THEN check which sum is max
        # sum of 2 -ve and one +ve (2 -v goives +ve else 3 -ve will be -ve) or sum of 3 positive
        nums.sort()
        return max(nums[0]*nums[1]*nums[2], nums[-1]*nums[-2]*nums[-3])


if __name__ == '__main__':
    sol = Solution()
    ans = sol.maximumProduct(
        [1,2,3])
    print(ans)
