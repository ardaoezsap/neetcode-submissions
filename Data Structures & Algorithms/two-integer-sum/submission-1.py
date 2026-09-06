class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in numbers:
                return [numbers[rest], i]
            else:
                numbers[nums[i]] = i