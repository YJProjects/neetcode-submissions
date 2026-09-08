"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        for idx in range(len(intervals)):
            intervals[idx] = [intervals[idx].start, intervals[idx].end]

        intervals.sort()

        for idx, interval in enumerate(intervals):
            if idx == len(intervals) - 1:
                continue

            if interval[1] > intervals[idx + 1][0]:
                return False

        return True
