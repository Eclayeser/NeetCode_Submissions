class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        length = len(nums)
        acc = 1
        left_to_right = []
        right_to_left = []
        for i in range(0, length-1):
            number = nums[i]
            acc = acc * number
            left_to_right.append(acc)
        acc = 1
        for i in range(0, length-1):
            i_backs = (length-1) - i
            number = nums[i_backs]
            acc = acc * number
            right_to_left.append(acc)
        pointer_l_r = -1
        pointer_r_l = length - 2
        for i in range(0, length):
            if pointer_l_r == -1:
                output.append(right_to_left[pointer_r_l])
            elif pointer_r_l == -1:
                output.append(left_to_right[pointer_l_r])
            else: 
                output.append(left_to_right[pointer_l_r]*right_to_left[pointer_r_l])
            pointer_l_r += 1
            pointer_r_l -= 1
        return output
