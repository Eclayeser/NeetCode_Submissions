class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap: dict[str, int] = {}
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
            else:
                return False

        for value in hashmap.values():
            if value != 0:
                return False
        
        return True