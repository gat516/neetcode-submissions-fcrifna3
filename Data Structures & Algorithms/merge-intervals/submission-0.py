class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #how to check if intervals overlap?
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        #ok, intervals are sorted by first index
        #once i move to the next index, check the last index

        for start, end in intervals[1:]:
            prevEnd = merged[-1][1]

            if start <= prevEnd:
                merged[-1][1] = max(prevEnd, end)
            else:
                merged.append([start,end])
        return merged