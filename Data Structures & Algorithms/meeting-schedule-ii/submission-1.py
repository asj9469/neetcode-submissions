"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # [[0,30], [5,10], [15,35],[31,45]] -> 2
        # {0: 1, 5: 1, ...}

        max_rooms = 0
        curr_count = 0
        seq_dict = {}
        
        # go through the intervals list and store in dictionary (+1 / -1)
        for interval in intervals:
            seq_dict[interval.start] = seq_dict.get(interval.start, 0) + 1
            seq_dict[interval.end] = seq_dict.get(interval.end, 0) - 1

            # 0,8
            # [(0,40),(5,10),(15,20)]
            
            # 0: 1, 5:1, 10:-1, 15:1, 20:-1, 40:-1


        # sort the keys

        # iterate through the dictionary while keeping max
        for key in sorted(seq_dict.keys()):
            curr_count += seq_dict[key]
            max_rooms = max(max_rooms, curr_count)

        # return count
        return max_rooms