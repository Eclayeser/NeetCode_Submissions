class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {(int, int, ...): [str, str, ... ], ...} - final_map
        # {count, count, count, ...} - str_sublist 
        # 97 - 122 ASCII chars as indexes for the str_sublist
        final_map: dict[tuple[int], list[str]] = {}
        ASCII_CONST = 97
        for string in strs:
            str_sublist: list[int] = [0 for n in range(0, 26)]
            for char in string:
                # convert to ASCII code for index
                str_sublist[ord(char) - ASCII_CONST] += 1
            key = tuple(str_sublist)
            sublist = final_map.get(key, [])
            sublist.append(string)
            final_map[key] = sublist
        list_to_return = list(final_map.values())
        return list_to_return
