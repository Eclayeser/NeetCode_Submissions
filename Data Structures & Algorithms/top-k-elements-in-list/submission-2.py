class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map: dict[int, int] = {} #{num: count, }
        return_list: list[int] = []
        for num in nums:
            # record count
            count = my_map.get(num, 0)
            count += 1
            my_map[num] = count
        values = list(my_map.values())
        keys = list(my_map.keys())
        for i in range(0, k):
            largest_index = values.index(max(values))
            values.pop(largest_index)
            return_list.append(keys.pop(largest_index))
        return return_list


