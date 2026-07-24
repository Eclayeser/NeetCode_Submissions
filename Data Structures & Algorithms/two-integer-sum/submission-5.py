class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage: dict[int, int] = {}
        for i in range(0, len(nums)):
            if nums[i] in storage.keys():
                return [storage[nums[i]], i]
            storage[target - nums[i]] = i
        return [-1, -1]