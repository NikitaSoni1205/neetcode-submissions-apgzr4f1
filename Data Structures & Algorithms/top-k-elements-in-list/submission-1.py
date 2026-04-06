class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for i in nums:
            if i not in frequencies:
                frequencies[i] = 1
            else:
                frequencies[i] = frequencies[i] + 1
        sorted_dict_desc = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_dict_desc)
        return list(sorted_dict_desc.keys())[:k]