from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ln = [len(x) for x in strs]
        if len(ln) == 0:
            return ""
        lcp = ""
        for i in range(min(ln)):
            current = strs[0]
            ok = False
            for st in strs[1:]:
                if current[i] == st[i]:
                    ok = True
                else:
                    ok = False
                    break
                current = st
            if ok:
                lcp += strs[0][i]
            else:
                break
        return lcp




if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["aca","cba"]))
