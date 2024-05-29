class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complements = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i
        return []

def main():
    solution = Solution()
    nums = [3,3]
    target = 6

    result = solution.twoSum(nums, target)
    print("Indices of the two numbers that add up to", target, "are:", result)

if __name__ == "__main__":
    main()