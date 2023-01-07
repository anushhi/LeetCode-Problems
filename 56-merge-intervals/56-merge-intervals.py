class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda x:(x[0],x[1]))
        ans = [intervals[0]]

        for start,end in intervals:
            if ans[-1][1] >= start:
                ans[-1][1] = max(ans[-1][1],end)
            else:
                ans.append([start,end])
                
        return ans
                
        