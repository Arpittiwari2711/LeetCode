class Solution(object):
    def insert(self, intervals, newInterval):
        result = []

        for i, interval in enumerate(intervals):

            # Current interval is completely before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Current interval is completely after newInterval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            # Overlapping intervals
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        result.append(newInterval)
        return result