class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)
        return res


if __name__ == '__main__':
    sol = Solution()
    ans = sol.merge(
        [[4, 5], [2, 4], [4, 6], [3, 4], [0, 0], [1, 1], [3, 5], [2, 2]]
    )
    print(ans)
