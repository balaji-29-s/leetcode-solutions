class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cnt=0
        endinterval=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<endinterval:
                cnt+=1
            else:
                endinterval=intervals[i][1]
        return cnt