## Day 31 - Two Sum (Python)

**Problem:**  
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

**Approach:**  
We use a **hashmap (dictionary in Python)** to achieve an efficient O(n) solution:
1. Iterate through the array while keeping track of each number’s index in a hashmap.
2. For each number, calculate its complement as `target - num`.
3. If the complement exists in the hashmap, return the stored index of the complement and the current index.
4. Otherwise, store the current number and its index in the hashmap for future lookups.

**Complexity:**  
- Time: O(n)  
- Space: O(n)  

**Example:**  
Input: `nums = [2,7,11,15], target = 9`  
Output: `[0,1]`
