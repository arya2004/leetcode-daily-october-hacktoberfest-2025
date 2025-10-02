import collections

class Solution(object):  # Use old-style class definition for Python 2/3 compatibility
    def numIdenticalPairs(self, nums):
        """
        Counts the number of good pairs (i, j) where nums[i] == nums[j] and i < j.
        """
        # Create a Counter (dictionary) to store the frequency of each number
        c = collections.Counter()
        
        # Initialize a variable to count the number of good pairs
        pairs = 0

        # Iterate through each number in the input list
        for x in nums:
            # Add the current count of x to pairs
            # Each previous occurrence of x can form a good pair with this x
            pairs += c[x]
            
            # Increment the count of the current number
            c[x] += 1

        # Return the total number of good pairs
        return pairs

# Example usage:
sol = Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))  # Output: 4
