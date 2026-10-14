class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            if num in seen: 
                seen[num] += 1
            else:
                seen[num] = 1


        unique_nums = list(seen.keys())
        unique_nums.sort(key=lambda x: seen[x], reverse=True)

        return unique_nums[:k]