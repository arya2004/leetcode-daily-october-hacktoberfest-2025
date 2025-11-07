import java.util.*;

class Solution {
    String s;            // Input string
    int n, K;            // n = length of string, K = max distinct characters allowed
    Map<Long, Integer> memo = new HashMap<>(); // Memoization map to store computed states

    // Main function to find the maximum number of partitions after at most one character change
    public int maxPartitionsAfterOperations(String _s, int k) {
    s = _s;
    n = s.length();
    K = k;
    memo.clear();

    // Start DFS from index 0, mask = 0, usedChange = 0
    return dfs(0, 0, 0) + 1;
}

    /**
     * Recursive DFS function.
     * @param i - current index in the string
     * @param mask - bitmask representing characters used in current partition
     * @param used - whether we've already used our one allowed character change (0 or 1)
     * @return maximum number of partitions from index i onwards
     */
    int dfs(int i, int mask, int used) {
        // Base case: reached end of string → no more partitions possible
        if (i >= n) return 0;

        // Unique key for memoization (combines i, mask, and used)
        long key = ((long) i << 32) | ((long) mask << 1) | used;
        if (memo.containsKey(key)) return memo.get(key);

        int res = 0;

        // --- Option 1: Use the current character as is ---
        int bit = 1 << (s.charAt(i) - 'a');  // Convert character to bit position (0–25)
        int newMask = mask | bit;            // Add this character to the bitmask

        // If number of distinct characters exceeds K → start new partition
        if (Integer.bitCount(newMask) > K)
            res = Math.max(res, 1 + dfs(i + 1, bit, used));
        else
            // Otherwise, continue in the same partition
            res = Math.max(res, dfs(i + 1, newMask, used));

        // --- Option 2: Change current character (only if not already used) ---
        if (used == 0) {
            for (int c = 0; c < 26; c++) {  // Try changing current char to any letter
                bit = 1 << c;
                newMask = mask | bit;

                // If exceeds K → new partition
                if (Integer.bitCount(newMask) > K)
                    res = Math.max(res, 1 + dfs(i + 1, bit, 1));
                else
                    // Otherwise continue with same partition
                    res = Math.max(res, dfs(i + 1, newMask, 1));
            }
        }

        // Store result in memo table to avoid recomputation
        memo.put(key, res);
        return res;
    }
}
