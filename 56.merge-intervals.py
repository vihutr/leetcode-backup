# @leet start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        i = 0
        start = None
        intervals = sorted(intervals)
        # intervals = deque(intervals)
        while i < len(intervals):
            if start is None:
                start = intervals[i]
            if i + 1 >= len(intervals):
                results.append(start)
                i += 1
                break
            if start[1] >= intervals[i + 1][0] and start[1] <= intervals[i + 1][1]:
                start[1] = intervals[i + 1][1]
            elif not start[1] > intervals[i + 1][1]:
                results.append(start)
                start = None
            i += 1
        return results

                
# @leet end
