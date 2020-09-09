from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache_s = {}
        for i in s:
            if cache_s.get(i) is None:
                cache_s[i] = 0
            cache_s[i] += 1
        cache_t = {}
        for i in t:
            if cache_t.get(i) is None:
                cache_t[i] = 0
            cache_t[i] += 1

        for (k,v) in cache_s.items():
            if cache_t.get(k) is None or cache_t[k] != v:
                return False
        for (k,v) in cache_t.items():
            if cache_s.get(k) is None or cache_s[k] != v:
                return False
        return True



if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
