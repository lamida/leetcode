from typing import List


class Solution:
    def rev(self, st: bytearray, start, stop):
        if start < stop - 1:
            st[start], st[stop - 1] = st[stop-1], st[start]
            self.rev(st, start + 1, stop - 1)

    def reverse(self, x: int) -> int:
        x = str(x)
        minus = False
        if x[0] == b"-":
            minus = True
            x = x[1:]
        s = bytearray()
        s.extend(map(ord, str(x)))
        self.rev(s, 0, len(s))
        num = int(s)
        if minus:
            num = -num
        if num > 2 ** 31 or num < -2 ** 31:
            return 0

        return num


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(4321))
