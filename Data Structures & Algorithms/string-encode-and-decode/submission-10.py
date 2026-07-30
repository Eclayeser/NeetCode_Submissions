class Solution:
    lengths: list[int] = []

    def encode(self, strs: List[str]) -> str:
        encoded_string: str = ""
        self.lengths = []
        for string in strs:
            self.lengths.append(len(string))
            encoded_string += string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs: list[str] = []
        low_index = 0
        for length in self.lengths:
            decoded_strs.append(s[low_index:length+low_index])
            low_index += length
        return decoded_strs