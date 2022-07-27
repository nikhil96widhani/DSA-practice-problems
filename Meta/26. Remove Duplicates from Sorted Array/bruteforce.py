class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer = 0
        while pointer+1 < len(nums):
            if nums[pointer] == nums[pointer + 1]:
                nums.pop(pointer + 1)
            else:
                pointer += 1

        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    ans = sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

    print(ans)
