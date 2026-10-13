class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for ind, val in enumerate(nums):

            sub = target - val
            if sub in seen:
                return [seen[sub], ind]

            seen[val] = ind