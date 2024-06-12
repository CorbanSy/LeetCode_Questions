class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If the merged list is empty or the current interval does not overlap with the last interval in merged
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, so merge the current interval with the last interval in merged
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged