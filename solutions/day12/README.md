# Python Interview Questions Collection

This directory contains a comprehensive collection of Python interview questions with optimized solutions covering various topics essential for technical interviews.

## 📋 Topics Covered

### 1. **Array and List Operations**
- Two Sum Problem
- Find Maximum Element
- Remove Duplicates
- Find Second Largest Element
- Merge Sorted Lists
- Reverse List In-Place
- Rotate Array

### 2. **String Manipulation**
- Reverse String
- Palindrome Check
- Anagram Detection
- Longest Common Prefix
- Valid Parentheses
- Character Frequency Count
- Word Frequency Counter

### 3. **Searching and Sorting**
- Binary Search Implementation
- Bubble Sort
- Quick Sort
- Merge Sort
- Find Peak Element

### 4. **Mathematical Problems**
- Fibonacci Series
- Prime Number Check
- Factorial Calculation
- Find Missing Number

### 5. **Data Structures**
- Stack Implementation
- Queue Implementation
- Find All Subsets
- Find All Permutations

### 6. **Advanced Topics**
- Email Validation
- Random Password Generation
- Duplicate Detection
- Mathematical Computations

## 🚀 Key Features

- **Type Hints**: All functions include proper type annotations
- **Optimized Solutions**: Time and space complexity optimized
- **Clean Code**: Well-documented and readable code
- **Error Handling**: Proper validation and exception handling
- **Multiple Approaches**: Various solution methods demonstrated
- **Test Cases**: Comprehensive test function included

## 💡 Complexity Analysis

| Problem | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Two Sum | O(n) | O(n) |
| Binary Search | O(log n) | O(1) |
| Fibonacci | O(n) | O(1) |
| Prime Check | O(√n) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg | O(log n) |
| Bubble Sort | O(n²) | O(1) |
| Subsets | O(2^n) | O(2^n) |
| Permutations | O(n!) | O(n!) |

## 🎯 Python-Specific Features Demonstrated

### 1. **List Comprehensions**
```python
left = [x for x in arr if x < pivot]
middle = [x for x in arr if x == pivot]
right = [x for x in arr if x > pivot]
```

### 2. **Built-in Functions**
```python
return max(arr)
return sorted(s1.lower()) == sorted(s2.lower())
return Counter(text)
```

### 3. **String Methods**
```python
s = ''.join(c.lower() for c in s if c.isalnum())
return s == s[::-1]
```

### 4. **Collections Module**
```python
from collections import defaultdict, Counter, deque
```

### 5. **Type Hints**
```python
def two_sum(self, nums: List[int], target: int) -> List[int]:
```

## 🔧 How to Run

### Prerequisites
- Python 3.7+ (for type hints support)
- No external dependencies required

### Execution
```bash
python PythonInterviewQuestions.py
```

## 📚 Learning Objectives

After studying this code collection, you will understand:

1. **Python Fundamentals**
   - List and string operations
   - Built-in functions and methods
   - Type hints and annotations

2. **Algorithm Implementation**
   - Sorting algorithms
   - Search algorithms
   - Recursive solutions

3. **Data Structures**
   - Stack and Queue implementation
   - List manipulation techniques
   - Set and dictionary operations

4. **Python Best Practices**
   - Code organization and structure
   - Error handling patterns
   - Performance optimization

5. **Advanced Python Features**
   - List comprehensions
   - Generator expressions
   - Collections module usage

## 🎯 Interview Tips

1. **Always explain your approach** before coding
2. **Consider edge cases** and handle them appropriately
3. **Optimize for time and space** complexity
4. **Use Python's built-in functions** when appropriate
5. **Write clean, readable code** with proper naming
6. **Test your solution** with different inputs

## 📝 Code Structure

The main class `PythonInterviewQuestions` contains:
- 30+ interview question solutions
- Helper classes (Stack, Queue)
- Comprehensive test function
- Type hints for all methods
- Detailed docstrings

## 🌟 Additional Resources

- Practice on LeetCode, HackerRank, or CodeSignal
- Study Python documentation for built-in functions
- Review data structures and algorithms
- Practice system design questions
- Learn about Python's GIL and performance characteristics

## 🔍 Key Python Concepts Demonstrated

- **List slicing**: `arr[::-1]` for reversing
- **Set operations**: For duplicate detection
- **Dictionary comprehensions**: For frequency counting
- **Lambda functions**: For sorting and filtering
- **Exception handling**: Try-except blocks
- **Module imports**: Collections and typing modules
- **Class methods**: Static and instance methods
- **String formatting**: f-strings and format methods

## 📊 Performance Considerations

- **Time Complexity**: Focus on algorithmic efficiency
- **Space Complexity**: Consider memory usage
- **Python-specific optimizations**: Use built-in functions
- **Data structure choices**: Lists vs sets vs dictionaries
- **Loop optimization**: Minimize nested loops when possible

## 🎓 Interview Preparation

This collection covers the most commonly asked Python interview questions:
- Array/List manipulation
- String processing
- Algorithm implementation
- Data structure operations
- Problem-solving approaches
- Code optimization techniques
