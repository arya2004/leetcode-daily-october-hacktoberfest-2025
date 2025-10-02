class Solution:
    def integerBreak(self, n):
        """
        Given an integer n, split it into the sum of at least two positive integers 
        and maximize the product of those integers.

        :param n: int
        :return: int (maximum product)
        """

        # Base case:
        # For n = 2 -> best split is (1+1) => product = 1
        # For n = 3 -> best split is (1+2) => product = 2
        if n <= 3:
            return n - 1

        # If n is divisible by 3, the best split is all 3's
        # Example: n = 9 -> 3+3+3 -> 3*3*3 = 27
        if n % 3 == 0:
            return 3 ** (n // 3)

        # If remainder is 1, it's better to convert "3 + 1" into "4"
        # Example: n = 10 -> 3+3+4 = 36 (better than 3+3+3+1 = 27)
        elif n % 3 == 1:
            return 4 * (3 ** ((n - 4) // 3))

        # If remainder is 2, just multiply by 2 at the end
        # Example: n = 8 -> 3+3+2 = 18
        else:  # n % 3 == 2
            return 2 * (3 ** ((n - 2) // 3))
