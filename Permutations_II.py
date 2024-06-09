class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
                return
            seen = set()
            for i in range(start, end):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1, end)
                    nums[start], nums[i] = nums[i], nums[start]

        nums.sort()  # Sort the array to handle duplicates easily
        result = []
        backtrack(0, len(nums))
        return result