# @leet start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        # add all intervals before current interval is relevant to newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # combine all intervals from relevant interval until newInterval becomes irrelevant
        mergedInterval = newInterval
        # check for len for edge case of empty intervals provided
        if i < len(intervals) and newInterval[0] > intervals[i][0]:
            mergedInterval[0] = intervals[i][0]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            if intervals[i][1] <= newInterval[1]:
                mergedInterval[1] = newInterval[1]
            else:
                mergedInterval[1] = intervals[i][1]
            i += 1
        res.append(mergedInterval)
        # add the rest of the intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
# @leet end
