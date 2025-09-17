# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final_intervals = []

        # 1. Sort the intervals by starting time first
        intervals.sort(key=lambda a: a[0])

        # 2. The idea is to create a "CONTINOUS" interval that expands (we init it to the first interval)
        current_start = intervals[0][0]
        current_end = intervals[0][1]

        # 3. go through all intervals
        for x in range(1, len(intervals), 1):
            interval = intervals[x]
            start = interval[0]
            end = interval[1]

            # 4. Check if this current interval overlaps with our interval so far
            if start <= current_end:
                if (
                    end > current_end
                ):  # 4.1 Expand the interval if this interval's end is longer than our current continous end
                    current_end = end
            else:
                # 5. No overlap, append old interval and create new interval
                final_intervals.append([current_start, current_end])
                current_start = start
                current_end = end

        # 6. We need to append the final continous interval as well
        final_intervals.append([current_start, current_end])
        return final_intervals
