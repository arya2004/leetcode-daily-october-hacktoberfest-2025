import java.util.*;

class Solution {
    String s;
    int n, K;
    Map<Long, Integer> memo = new HashMap<>();

    public int maxPartitionsAfterOperations(String _s, int k) {
        s = _s;
        n = s.length();
        K = k;
        memo.clear();
        return dfs(0, 0, 0) + 1;
    }

    int dfs(int i, int mask, int used) {
        if (i >= n) return 0;
        long key = ((long) i << 32) | ((long) mask << 1) | used;
        if (memo.containsKey(key)) return memo.get(key);
        int res = 0;
        int bit = 1 << (s.charAt(i) - 'a');
        int newMask = mask | bit;
        if (Integer.bitCount(newMask) > K)
            res = Math.max(res, 1 + dfs(i + 1, bit, used));
        else
            res = Math.max(res, dfs(i + 1, newMask, used));
        if (used == 0) {
            for (int c = 0; c < 26; c++) {
                bit = 1 << c;
                newMask = mask | bit;
                if (Integer.bitCount(newMask) > K)
                    res = Math.max(res, 1 + dfs(i + 1, bit, 1));
                else
                    res = Math.max(res, dfs(i + 1, newMask, 1));
            }
        }
        memo.put(key, res);
        return res;
    }
}
