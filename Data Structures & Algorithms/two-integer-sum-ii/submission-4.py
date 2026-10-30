class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while left_pointer < right_pointer:
            num_sum = numbers[left_pointer] + numbers[right_pointer]
            if num_sum == target:
                return [left_pointer+1, right_pointer+1]
            elif num_sum > target:
                right_pointer -= 1
            else:
                left_pointer += 1
