class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(heights) - 1
        max_Area = 0
        while left_pointer < right_pointer:
            diff = heights[left_pointer] - heights[right_pointer]
            area = min(heights[left_pointer],heights[right_pointer])*(right_pointer-left_pointer)
            if area > max_Area:
                max_Area = area

            if diff > 0:
                # left column higher
                right_pointer -= 1
            else:
                left_pointer += 1

        return max_Area