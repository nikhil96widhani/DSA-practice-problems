class Solution(object):
    def __init__(self):
        self.seen = {}

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            if target - num in self.seen:
                return [self.seen[target - num], i]
            elif num not in self.seen:
                self.seen[num] = i


if __name__ == '__main__':
    sol = Solution()
    ans = sol.twoSum([0, 4, 3, 0], 0)
    print(ans)
