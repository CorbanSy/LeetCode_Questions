class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Sort the array to simplify the two-pointer approach and avoid duplicates
        nums.sort()
        n = len(nums)
        result = []
        
        # Iterate through the array with two fixed elements
        for i in range(n):
            # Skip duplicate elements to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # Skip duplicate elements to avoid duplicate quadruplets
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two-pointer approach for the remaining two elements
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for left and right pointers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move pointers after finding a valid quadruplet
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result