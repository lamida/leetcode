from typing import List


class Solution:

    def firstUniqChar(self, s: str) -> int:
        cache = {}
        for i in s:
            if cache.get(i) is None:
                cache[i] = 0
            else:
                cache[i] += 1

        for x in range(len(s)):
            i = s[x]
            if cache[i] == 0:
                return x
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("loveleetcode"))
