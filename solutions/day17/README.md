## 🧠 LeetCode October Daily Challenge – Day XX

### 🏷️ Problem: Maximum Number of Partitions After One Character Change

You are given a string `s` and an integer `k`.

- You can split the string into multiple partitions where each partition contains **at most `k` distinct characters**.  
- You are allowed to **change at most one character** in the string (to any other lowercase letter).  
- Your task is to find the **maximum number of partitions** you can make after performing at most one character change.

Return the **maximum number of partitions** possible.

---

### 💡 Approach:

1. Use **Depth-First Search (DFS)** with **memoization** to explore all valid partition possibilities.  
2. Maintain a **bitmask** representing the distinct characters currently in the active partition.  
3. For each character:
   - Continue in the same partition if the distinct character count ≤ `k`.
   - Start a new partition when adding a new character would exceed `k`.  
4. Also consider applying **one character change** (used at most once) to increase the total number of partitions.  
5. Memoize each state `(index, bitmask, usedChange)` to prevent recomputation.

This approach ensures an optimal and efficient exploration of all possible splits.

---

### 🔧 Solution Details:
- **Languages Used:** C++, Java, Python  
- **Time Complexity:** O(n × 2²⁶ × 2) (effectively pruned using memoization)  
- **Space Complexity:** O(n × 2²⁶ × 2) (for recursion stack and memo table)  

---

### 🌟 Additional Notes:
- Handles all edge cases, including:
  - Repeated and unique character combinations  
  - Cases where `k` ≥ total unique letters in the string  
  - Short or long strings  
- Memoization ensures significant performance gains compared to a naive recursive approach.  
- Produces consistent and correct results across all supported languages.  

---

✅ *Solutions available in **C++**, **Java**, and **Python**, all following the same DFS + Memoization logic and yielding identical outputs.*
