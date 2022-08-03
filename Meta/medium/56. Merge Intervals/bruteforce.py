class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # if list has one interval then return intervals

        if len(intervals) == 1:
            return intervals
        # sort the intervals in increasing order
        else:
            intervals = sorted(intervals, key=lambda x: x[0])
        # Then try loop to check if intervals are present
        i = 0
        while i < len(intervals) - 1:
            # if second value of i interval is greater than first value of the next interval
            if intervals[i][1] >= intervals[i + 1][0]:
                # The second value also should be less than the second value of the next interval
                if intervals[i][1] <= intervals[i + 1][1]:
                    temp = [intervals[i][0], intervals[i + 1][1]]
                    del intervals[i]
                    del intervals[i]
                    intervals.insert(i, temp)
                # means next interval is same as first interval thenn delete the next interval
                else:
                    del intervals[i+1]
            else:
                i += 1
        return intervals


if __name__ == '__main__':
    sol = Solution()
    ans = sol.merge(
        [[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]
    )

    print(ans)
