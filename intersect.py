from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        skip_i = []
        skip_j = []
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and i not in skip_i and j not in skip_j:
                    skip_i.append(i)
                    skip_j.append(j)
                    res.append(nums1[i])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
    print(s.intersect([4, 9, 5], [9,4,9,8,4]))
