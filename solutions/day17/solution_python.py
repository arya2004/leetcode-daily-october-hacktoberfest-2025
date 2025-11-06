class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        # Store the string and parameters for use in recursion
        self.s = s
        self.n = len(s)
        self.K = k

        # Memoization dictionary to cache results of (index, mask, usedChange)
        self.memo = {}

        # Start DFS from index 0, with an empty mask (0) and usedChange = 0 (no change yet)
        # +1 because number of partitions = number of cuts + 1
        return self.dfs(0, 0, 0) + 1

    def dfs(self, i, mask, used):
        """
        Depth-First Search to find the maximum number of partitions.
        Args:
            i: current index in the string
            mask: bitmask of characters in the current partition
            used: whether the character change has been used (0 or 1)
        Returns:
            Maximum number of partitions from index i onwards
        """

        # Base case: reached end of the string → no more partitions
        if i >= self.n:
            return 0

        # Create a unique key for memoization using i, mask, and used
        key = (i << 32) | (mask << 1) | used
        if key in self.memo:
            return self.memo[key]

        res = 0  # Stores the best result for this state

        # ---- Option 1: Use the current character as it is ----
        bit = 1 << (ord(self.s[i]) - 97)  # Convert 'a'..'z' to bit positions 0..25
        newMask = mask | bit               # Add this character to the current partition

        # If distinct count exceeds K, start a new partition
        if bin(newMask).count('1') > self.K:
            res = max(res, 1 + self.dfs(i + 1, bit, used))
        else:
            # Otherwise, continue building the same partition
            res = max(res, self.dfs(i + 1, newMask, used))

        # ---- Option 2: Change this character (if not used yet) ----
        if used == 0:
            # Try changing the current character to any of the 26 letters
            for c in range(26):
                bit = 1 << c
                newMask = mask | bit

                # If distinct count exceeds K after change → new partition
                if bin(newMask).count('1') > self.K:
                    res = max(res, 1 + self.dfs(i + 1, bit, 1))
                else:
                    # Otherwise, continue same partition after using the change
                    res = max(res, self.dfs(i + 1, newMask, 1))

        # Store the computed result for this state to avoid re-computation
        self.memo[key] = res
        return res
