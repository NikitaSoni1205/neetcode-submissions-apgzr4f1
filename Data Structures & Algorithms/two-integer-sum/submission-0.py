class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in s:
                return [s[complement], index]

            s[value] = index