class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i in range(len(nums)):
            if nums[i] in frequency:
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1
        
        sortedNums = sorted(frequency, key= lambda x: frequency[x], reverse = True)

        return sortedNums[:k]

        
        