from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            current = nums[i]
            if cache.get(current) is not None:
                return [cache[current], i]
            cache[target-current] = i
        return []

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3,2,4], 6))
