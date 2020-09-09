from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        buffer = nums[-k:]
        for i in range(len(nums)-1, k-1, -1):
            nums[i] = nums[i-k]
        for i in range(len(buffer)):
            nums[i] = buffer[i]
        return None


if __name__ == "__main__":
    s = Solution()
    iin = [1,2,3,4,5,6,7]
    iin = [1,2]
    #[1,2,3,4,5,6,7]
    #[7,1,2,3,4,5,6]
    print(iin)
    s.rotate(iin, 3)
    print(iin)

