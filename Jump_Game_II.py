class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            # Update the farthest point that can be reached
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump,
            # increase the jump count and update the end point
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can reach or go beyond the last element, break early
                if current_end >= n - 1:
                    break
        
        return jumps