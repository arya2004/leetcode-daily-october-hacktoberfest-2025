class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers (nums) and an integer (target),
        return the indices of the two numbers such that they add up to target.
        
        Approach: Use a hashmap (dictionary in Python) to store numbers we’ve seen so far
        along with their indices, so we can check in O(1) if the complement exists.
        """

        # Dictionary to store numbers we've seen so far and their indices
        seen = {}

        # Loop through the list while keeping track of the index (i) and the value (num)
        for i, num in enumerate(nums):

            # The number we need to reach the target
            comp = target - num

            # Check if the complement is already in the dictionary
            if comp in seen:
                # If yes, return the index of the complement and the current index
                return [seen[comp], i]

            # Otherwise, store the current number with its index
            seen[num] = i

        # If no solution is found (though the problem guarantees one), return empty list
        return []
