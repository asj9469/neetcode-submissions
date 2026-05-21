class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        # [[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]
        #     0        1        2         0         1


        # meetings=[[1,20],[2,10],[3,5],[6,8],[4,9]]

        # sort the meetings
        meetings.sort()

        # create 2 arrays (roomUse & end time)
        endTime = [0] * n
        roomUse = [0] * n

        # iterate through all the meetings
        # for each meeting, go through endTime & update both arrays
        for m_start, m_end in meetings:
            found = False
            
            # this loop accounts for cases where you can replace the endtime OR you found an empty room
            for i, room_end in enumerate(endTime):
                if m_start >= room_end:
                    endTime[i] = m_end # update to the new end time
                    roomUse[i] += 1
                    found = True
                    break
            
            # if we didn't find one (all occupied), fast forward to the min end time & adjust accordingly
            if not found:
                minEndTime = min(endTime)
                minEndPos = endTime.index(minEndTime)
                
                endTime[minEndPos] = minEndTime + (m_end - m_start) # adjusting the endTime
                roomUse[minEndPos] += 1

        m_use = max(roomUse)
        for i, n in enumerate(roomUse):
            if n == m_use:
                return i
