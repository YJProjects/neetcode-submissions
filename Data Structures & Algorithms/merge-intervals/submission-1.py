class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        
        idx = 0
        res = []
        intervals.sort()
        
        while idx < len(intervals):
            newInterval = [intervals[idx][0], intervals[idx][1]]
            while idx + 1 < len(intervals) and newInterval[1] >= intervals[idx + 1][0]:
                newInterval[0] = min(newInterval[0], intervals[idx + 1][0])
                newInterval[1] = max(newInterval[1], intervals[idx + 1][1])
                idx += 1

            res.append(newInterval)
            idx += 1

        return res

        