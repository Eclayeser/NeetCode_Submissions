class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            left_char = s[left_pointer].lower()
            print(left_char)
            if not(left_char.isalnum()):
                left_pointer += 1
                continue
            right_char = s[right_pointer].lower()
            if not(right_char.isalnum()):
                right_pointer -= 1
                continue 
            if left_char != right_char:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True