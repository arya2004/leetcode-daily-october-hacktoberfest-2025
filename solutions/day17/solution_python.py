class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        self.s = s
        self.n = len(s)
        self.K = k
        self.memo = {}
        return self.dfs(0, 0, 0) + 1

    def dfs(self, i, mask, used):
        if i >= self.n:
            return 0
        key = (i << 32) | (mask << 1) | used
        if key in self.memo:
            return self.memo[key]
        res = 0
        bit = 1 << (ord(self.s[i]) - 97)
        newMask = mask | bit
        if bin(newMask).count('1') > self.K:
            res = max(res, 1 + self.dfs(i + 1, bit, used))
        else:
            res = max(res, self.dfs(i + 1, newMask, used))
        if used == 0:
            for c in range(26):
                bit = 1 << c
                newMask = mask | bit
                if bin(newMask).count('1') > self.K:
                    res = max(res, 1 + self.dfs(i + 1, bit, 1))
                else:
                    res = max(res, self.dfs(i + 1, newMask, 1))
        self.memo[key] = res
        return res
