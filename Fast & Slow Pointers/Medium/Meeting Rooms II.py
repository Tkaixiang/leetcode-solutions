# Sweep Lines/Intervals
# https://neetcode.io/problems/meeting-schedule-ii

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sweep Lines
        # Sort the start and end timings SEPERATELY first
        # (0,40),(5,45),(40,60),(45,70)
        # -> Start: 0,  5,40,45
        # -> End  : 40,45,60,70
        #
        # - current_start pointer
        #    -> Keep start that DOESNT conflict with the end (else we start += 1 until it doesnt)
        # - current_end pointer
        #    ->
        #  ---------------
        #  start[current_start] < end[current_end]
        #  running += 1
        #  current_start += 1 [0->5]
        #  current_start -> current_end = [5,40]
        # -> Effectively comparing the NEXT START of (5,45) to the CURRENT END of (0,40)
        #  ---------------
        #  start[current_start] < end[current_end] 
        #  running += 1
        #  current_start += 1 [5->40]
        #  -> Effectively comparing the NEXT START of (40,60) to the CURRENT END of (0,40)
        #  ---------------
        #  start[current_start] >= end[current_end] (0,40) Conflict resolved, doesnt collide with (40,60)
        #  running -= 1
        #  current_end += 1 [40 -> 45]
        #  -> Effectively comparing the NEXT END (5,45) to the CURRENT START (40,60)
        #  --------------
        #  start[current_start] < end[current_end] Conflict! (40,60) conflicts with (5,45)
        #  running += 1
        #  current_start += 1 [40 -> 45]
        #  -> Effectively comparing the NEXT START (45,70) to the CURRENT END (5,45)
        #  --------------
        #  start[current_start] >= end[current_end] 
        #  running -= 1
        #  current_end += 1 [45 -> 60]
        #  -> Effectively comparing the NEXT END (40,60) to the CURRENT START (45,70)
        #  -------------
        #  start[current_start] < end[current_end] (45,70) conflicts with (40,60)
        #  running += 1
        #  current_start += 1 [60 -> END: out of range]
        # ENDED

        start_timings = []
        end_timings = []
        for interval in intervals:
            start_timings.append(interval.start)
            end_timings.append(interval.end)
        
        start_timings.sort()
        end_timings.sort()

        current_start = current_end = 0
        currently_running_procs = 0
        max_procs = 0
        while (current_start < len(intervals)):
            if start_timings[current_start] < end_timings[current_end]:
                currently_running_procs += 1
                # Compare current_end with "next start" to check for conflicts
                current_start += 1
                if currently_running_procs > max_procs:
                    max_procs = currently_running_procs
            else:
                currently_running_procs -= 1
                # Conflict resolved! current_end does not conflict with the current_start
                # Compare "next end" with the current start
                current_end += 1

        return max_procs

            