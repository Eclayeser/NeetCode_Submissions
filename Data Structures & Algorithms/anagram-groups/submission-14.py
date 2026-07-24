class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {hash: [str, ... ], ...} - final_map
        # {letter: count, letter: count, letter: count, ...} - string_map
        # 97 - 122 ASCII chars
        final_map: dict[str, list[str]] = {}
        string_map: dict[str, int] = {}
        string_map_default = {chr(n): 0 for n in range(97, 123)}
        for string in strs:
            string_map = string_map_default.copy()
            for char in string:
                # count = string_map.get(char, 0)
                string_map[char] += 1
            hash_id = self.hashDict(string_map)
            print(hash_id)
            sublist = final_map.get(hash_id, [])
            sublist.append(string)
            final_map[hash_id] = sublist
        list_to_return = list(final_map.values())
        return list_to_return

    def hashDict(self, string_map: dict[str, int]) -> str:
        hash_id: str = ""
        for k, v in string_map.items():
            hash_id += k + str(v)
        return hash_id
