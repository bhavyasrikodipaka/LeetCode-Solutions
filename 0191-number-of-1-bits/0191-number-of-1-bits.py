class Solution:
    def hammingWeight(self, n: int) -> int:
        if (n == 0):
            return 0
        c = 0
        while (n != 0):
            n = n & (n - 1)
            c += 1
        return c