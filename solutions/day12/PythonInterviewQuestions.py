"""
Comprehensive Python Interview Questions Collection
This file contains solutions to common Python interview questions
covering various topics like data structures, algorithms, OOP, etc.
"""

import sys
from collections import defaultdict, Counter, deque
from typing import List, Dict, Optional, Tuple
import math
import random

class PythonInterviewQuestions:
    
    # 1. Two Sum Problem
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in array that add up to target.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
    # 2. Reverse String
    def reverse_string(self, s: str) -> str:
        """
        Reverse a string using slicing.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        return s[::-1]
    
    # 3. Check if String is Palindrome
    def is_palindrome(self, s: str) -> bool:
        """
        Check if string is palindrome (ignoring case and non-alphanumeric).
        Time Complexity: O(n), Space Complexity: O(1)
        """
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
    
    # 4. Find Maximum Element in List
    def find_max(self, arr: List[int]) -> int:
        """
        Find maximum element in list.
        Time Complexity: O(n), Space Complexity: O(1)
        """
        if not arr:
            raise ValueError("List cannot be empty")
        return max(arr)
    
    # 5. Binary Search Implementation
    def binary_search(self, arr: List[int], target: int) -> int:
        """
        Binary search implementation.
        Time Complexity: O(log n), Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    # 6. Fibonacci Series
    def fibonacci(self, n: int) -> int:
        """
        Calculate nth Fibonacci number using dynamic programming.
        Time Complexity: O(n), Space Complexity: O(1)
        """
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    
    # 7. Check if Number is Prime
    def is_prime(self, n: int) -> bool:
        """
        Check if number is prime.
        Time Complexity: O(√n), Space Complexity: O(1)
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        
        return True
    
    # 8. Factorial Calculation
    def factorial(self, n: int) -> int:
        """
        Calculate factorial of a number.
        Time Complexity: O(n), Space Complexity: O(1)
        """
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n <= 1:
            return 1
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        
        return result
    
    # 9. Remove Duplicates from List
    def remove_duplicates(self, arr: List[int]) -> List[int]:
        """
        Remove duplicates while preserving order.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        seen = set()
        result = []
        for num in arr:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result
    
    # 10. Check if Two Strings are Anagrams
    def are_anagrams(self, s1: str, s2: str) -> bool:
        """
        Check if two strings are anagrams.
        Time Complexity: O(n log n), Space Complexity: O(1)
        """
        return sorted(s1.lower()) == sorted(s2.lower())
    
    # 11. Find Second Largest Element
    def find_second_largest(self, arr: List[int]) -> int:
        """
        Find second largest element in list.
        Time Complexity: O(n), Space Complexity: O(1)
        """
        if len(arr) < 2:
            raise ValueError("List must have at least 2 elements")
        
        largest = second_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        
        if second_largest == float('-inf'):
            raise ValueError("No second largest element found")
        
        return second_largest
    
    # 12. Merge Two Sorted Lists
    def merge_sorted_lists(self, list1: List[int], list2: List[int]) -> List[int]:
        """
        Merge two sorted lists into one sorted list.
        Time Complexity: O(m + n), Space Complexity: O(m + n)
        """
        result = []
        i = j = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        
        result.extend(list1[i:])
        result.extend(list2[j:])
        
        return result
    
    # 13. Count Character Frequency
    def count_character_frequency(self, text: str) -> Dict[str, int]:
        """
        Count frequency of each character in string.
        Time Complexity: O(n), Space Complexity: O(k) where k is unique chars
        """
        return Counter(text)
    
    # 14. Check if List Contains Duplicates
    def contains_duplicates(self, arr: List[int]) -> bool:
        """
        Check if list contains duplicates.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        return len(arr) != len(set(arr))
    
    # 15. Find Missing Number in Range 1 to n
    def find_missing_number(self, arr: List[int], n: int) -> int:
        """
        Find missing number in array containing numbers 1 to n.
        Time Complexity: O(n), Space Complexity: O(1)
        """
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum
    
    # 16. Reverse List In-Place
    def reverse_list(self, arr: List[int]) -> List[int]:
        """
        Reverse list in-place.
        Time Complexity: O(n), Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
    
    # 17. Find Longest Common Prefix
    def longest_common_prefix(self, strs: List[str]) -> str:
        """
        Find longest common prefix among strings.
        Time Complexity: O(S) where S is sum of all characters, Space Complexity: O(1)
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
    
    # 18. Valid Parentheses
    def is_valid_parentheses(self, s: str) -> bool:
        """
        Check if parentheses are valid.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack
    
    # 19. Find Peak Element
    def find_peak_element(self, nums: List[int]) -> int:
        """
        Find peak element in array.
        Time Complexity: O(log n), Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    # 20. Rotate Array
    def rotate_array(self, nums: List[int], k: int) -> None:
        """
        Rotate array to the right by k steps.
        Time Complexity: O(n), Space Complexity: O(1)
        """
        n = len(nums)
        k = k % n
        
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
    
    # 21. Implement Stack using List
    class Stack:
        def __init__(self):
            self.items = []
        
        def push(self, item):
            self.items.append(item)
        
        def pop(self):
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self.items.pop()
        
        def peek(self):
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self.items[-1]
        
        def is_empty(self):
            return len(self.items) == 0
        
        def size(self):
            return len(self.items)
    
    # 22. Implement Queue using List
    class Queue:
        def __init__(self):
            self.items = deque()
        
        def enqueue(self, item):
            self.items.append(item)
        
        def dequeue(self):
            if self.is_empty():
                raise IndexError("Queue is empty")
            return self.items.popleft()
        
        def front(self):
            if self.is_empty():
                raise IndexError("Queue is empty")
            return self.items[0]
        
        def is_empty(self):
            return len(self.items) == 0
        
        def size(self):
            return len(self.items)
    
    # 23. Bubble Sort Implementation
    def bubble_sort(self, arr: List[int]) -> List[int]:
        """
        Bubble sort implementation.
        Time Complexity: O(n²), Space Complexity: O(1)
        """
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    
    # 24. Quick Sort Implementation
    def quick_sort(self, arr: List[int]) -> List[int]:
        """
        Quick sort implementation.
        Time Complexity: O(n log n) average, O(n²) worst, Space Complexity: O(log n)
        """
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return self.quick_sort(left) + middle + self.quick_sort(right)
    
    # 25. Merge Sort Implementation
    def merge_sort(self, arr: List[int]) -> List[int]:
        """
        Merge sort implementation.
        Time Complexity: O(n log n), Space Complexity: O(n)
        """
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        return self.merge_sorted_lists(left, right)
    
    # 26. Find All Subsets
    def find_subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Find all possible subsets of array.
        Time Complexity: O(2^n), Space Complexity: O(2^n)
        """
        result = []
        
        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result
    
    # 27. Find All Permutations
    def find_permutations(self, nums: List[int]) -> List[List[int]]:
        """
        Find all permutations of array.
        Time Complexity: O(n!), Space Complexity: O(n!)
        """
        result = []
        
        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()
        
        backtrack([])
        return result
    
    # 28. Word Frequency Counter
    def word_frequency(self, text: str) -> Dict[str, int]:
        """
        Count frequency of words in text.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        words = text.lower().split()
        return Counter(words)
    
    # 29. Check if String is Valid Email
    def is_valid_email(self, email: str) -> bool:
        """
        Check if string is valid email format.
        Time Complexity: O(1), Space Complexity: O(1)
        """
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    # 30. Generate Random Password
    def generate_password(self, length: int = 12) -> str:
        """
        Generate random password with letters, digits, and symbols.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        import string
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

# Test function to demonstrate functionality
def test_python_interview_questions():
    """Test function to demonstrate all solutions"""
    solution = PythonInterviewQuestions()
    
    # Test Two Sum
    nums = [2, 7, 11, 15]
    result = solution.two_sum(nums, 9)
    print(f"Two Sum Result: {result}")
    
    # Test Reverse String
    print(f"Reverse String: {solution.reverse_string('hello')}")
    
    # Test Palindrome
    print(f"Is Palindrome: {solution.is_palindrome('A man a plan a canal Panama')}")
    
    # Test Fibonacci
    print(f"Fibonacci(10): {solution.fibonacci(10)}")
    
    # Test Prime
    print(f"Is Prime(17): {solution.is_prime(17)}")
    
    # Test Factorial
    print(f"Factorial(5): {solution.factorial(5)}")
    
    # Test Stack
    stack = solution.Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack pop: {stack.pop()}")
    print(f"Stack peek: {stack.peek()}")
    
    # Test Queue
    queue = solution.Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue dequeue: {queue.dequeue()}")
    print(f"Queue front: {queue.front()}")
    
    # Test Sorting
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Bubble Sort: {solution.bubble_sort(arr.copy())}")
    print(f"Quick Sort: {solution.quick_sort(arr.copy())}")
    print(f"Merge Sort: {solution.merge_sort(arr.copy())}")
    
    # Test Subsets
    print(f"Subsets of [1,2,3]: {solution.find_subsets([1, 2, 3])}")
    
    # Test Word Frequency
    text = "hello world hello python world"
    print(f"Word Frequency: {solution.word_frequency(text)}")
    
    # Test Email Validation
    print(f"Valid Email: {solution.is_valid_email('test@example.com')}")
    
    # Test Password Generation
    print(f"Generated Password: {solution.generate_password(8)}")

if __name__ == "__main__":
    test_python_interview_questions()
