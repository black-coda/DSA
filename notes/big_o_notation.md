Perfect! Let's start with the absolute fundamentals. I'll make this super practical and intuitive.

# Part 1: Big O Notation (Understanding Performance)

## What is Big O?

Big O tells you **how your algorithm's performance scales** as the input size grows. It's not about exact time, but about the **growth rate**.

Think of it like this:
- You're organizing books on a shelf
- Big O answers: "If I have 10x more books, how much longer will it take?"

## Common Big O Notations (From Best to Worst)

### **O(1) - Constant Time**
"No matter how much data, always takes the same time"

```python
def get_first_element(arr):
    return arr[0]  # Always one operation, whether arr has 10 or 1 million items

# Examples:
# arr = [1, 2, 3] → takes 1 operation
# arr = [1, 2, 3, ..., 1000000] → still takes 1 operation
```

**Real life**: Looking up a phone contact by scrolling to their name in your favorites (you saved their position)

---

### **O(log n) - Logarithmic Time**
"Doubles the input, only adds one more step"

```python
# We'll see this with binary search soon!
# If you have 100 items → ~7 comparisons
# If you have 1,000 items → ~10 comparisons
# If you have 1,000,000 items → ~20 comparisons
```

**Real life**: Looking up a word in a dictionary (you keep halving the pages)

---

### **O(n) - Linear Time**
"Double the input, double the time"

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # Must check every element
        if num > max_val:
            max_val = num
    return max_val

# arr with 10 items → 10 operations
# arr with 100 items → 100 operations
# arr with 1000 items → 1000 operations
```

**Real life**: Reading every book to find the one with the most pages

---

### **O(n log n) - Linearithmic Time**
"Efficient sorting algorithms"

```python
# Merge sort, quicksort (we'll learn these later)
# 100 items → ~664 operations
# 1000 items → ~9,966 operations
```

**Real life**: Sorting a deck of cards efficiently

---

### **O(n²) - Quadratic Time**
"Nested loops - very slow for large inputs"

```python
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):           # n times
        for j in range(i + 1, len(arr)): # n times for each i
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
    return duplicates

# 10 items → ~100 operations
# 100 items → ~10,000 operations
# 1000 items → ~1,000,000 operations (yikes!)
```

**Real life**: Comparing every student's test score to every other student's score

---

### **O(2ⁿ) - Exponential Time**
"Avoid this! Doubles with each new input"

```python
# Recursive Fibonacci (bad implementation)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# n=10 → 177 operations
# n=20 → 21,891 operations
# n=30 → 2,692,537 operations (💀)
```

**Real life**: Trying every possible combination of a password

---

## Visual Comparison

```
Operations needed for different input sizes:

n = 10:
O(1)      → 1
O(log n)  → 3
O(n)      → 10
O(n log n)→ 33
O(n²)     → 100
O(2ⁿ)     → 1,024

n = 100:
O(1)      → 1
O(log n)  → 7
O(n)      → 100
O(n log n)→ 664
O(n²)     → 10,000
O(2ⁿ)     → 1,267,650,600,228,229,401,496,703,205,376 (☠️)

n = 1,000:
O(1)      → 1
O(log n)  → 10
O(n)      → 1,000
O(n log n)→ 9,966
O(n²)     → 1,000,000
O(2ⁿ)     → (Universe heat death before completion)
```

---

## Rules for Calculating Big O

### Rule 1: Drop Constants
```python
def example(arr):
    print(arr[0])      # O(1)
    print(arr[0])      # O(1)
    print(arr[0])      # O(1)
    # Total: O(3) → We say O(1)
```
**Why?** Big O cares about growth rate, not exact operations

### Rule 2: Drop Non-Dominant Terms
```python
def example(arr):
    # Part 1: O(n)
    for item in arr:
        print(item)
    
    # Part 2: O(n²)
    for i in arr:
        for j in arr:
            print(i, j)
    
    # Total: O(n + n²) → We say O(n²)
```
**Why?** As n grows, n² dominates

### Rule 3: Different Inputs = Different Variables
```python
def example(arr1, arr2):
    for item in arr1:  # O(a) where a = len(arr1)
        print(item)
    
    for item in arr2:  # O(b) where b = len(arr2)
        print(item)
    
    # Total: O(a + b), NOT O(n)
```

---

# Part 2: Arrays

## What is an Array?

An array is a **contiguous block of memory** that stores elements of the same type.

```
Memory addresses:  1000  1004  1008  1012  1016
Array values:      [10] [20] [30] [40] [50]
Array indices:      0     1     2     3     4
```

## Array Operations & Their Big O

### 1. **Access by Index - O(1)**
```python
arr = [10, 20, 30, 40, 50]
print(arr[2])  # 30 - instant access

# Why O(1)?
# Computer calculates: base_address + (index × element_size)
# 1000 + (2 × 4) = 1008 → value is 30
# Same calculation time regardless of array size!
```

### 2. **Search (Find a Value) - O(n)**
```python
def linear_search(arr, target):
    for i in range(len(arr)):  # Might need to check every element
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
linear_search(arr, 40)  # Worst case: check all 5 elements

# Why O(n)?
# In worst case, target is at the end or not present
# Must check all n elements
```

### 3. **Insert at End - O(1)** (if space available)
```python
arr = [10, 20, 30]
arr.append(40)  # [10, 20, 30, 40]

# Why O(1)?
# Just put value in next position
# No other elements affected
```

### 4. **Insert at Beginning/Middle - O(n)**
```python
arr = [10, 20, 30, 40, 50]
arr.insert(0, 5)  # [5, 10, 20, 30, 40, 50]

# Why O(n)?
# Must shift ALL elements to the right:
# Step 1: 50 moves to position 5
# Step 2: 40 moves to position 4
# Step 3: 30 moves to position 3
# Step 4: 20 moves to position 2
# Step 5: 10 moves to position 1
# Step 6: 5 goes to position 0
# Total: n operations
```

### 5. **Delete - O(n)**
```python
arr = [10, 20, 30, 40, 50]
arr.remove(20)  # [10, 30, 40, 50]

# Why O(n)?
# After deleting 20, must shift everything left:
# 30 → position 1
# 40 → position 2
# 50 → position 3
```

---

## Practice: Analyze These Functions

```python
# Example 1: What's the Big O?
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

# Answer: O(n²) - nested loops, each go through entire array


# Example 2: What's the Big O?
def print_first_and_all(arr):
    print(arr[0])        # O(1)
    
    for item in arr:     # O(n)
        print(item)

# Answer: O(1 + n) → O(n) - we drop constants


# Example 3: What's the Big O?
def sum_array(arr):
    total = 0           # O(1)
    for num in arr:     # O(n)
        total += num    # O(1)
    return total        # O(1)

# Answer: O(n) - one loop through array
```

---

# Part 3: Binary Search (O(log n) Magic!)

## The Problem

```python
# You have a SORTED array
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]

# Find: Is 23 in the array? What's its index?

# BAD approach (Linear Search):
def linear_search(arr, target):
    for i in range(len(arr)):  # O(n) - check each element
        if arr[i] == target:
            return i
    return -1

# For 11 elements, might take 11 checks! 😞
```

## The Solution: Binary Search

**Key Insight**: Array is SORTED, so we can eliminate half the elements with each comparison!

### How It Works (Like Guessing a Number 1-100)

```
You think of 67. I guess:

Guess 1: "Is it 50?" → "Higher!"
Now I know: it's in [51-100], eliminated [1-50]

Guess 2: "Is it 75?" → "Lower!"
Now I know: it's in [51-74], eliminated [75-100]

Guess 3: "Is it 62?" → "Higher!"
Now I know: it's in [63-74]

Guess 4: "Is it 68?" → "Lower!"
Now I know: it's in [63-67]

Guess 5: "Is it 65?" → "Higher!"
Now I know: it's in [66-67]

Guess 6: "Is it 66?" → "Higher!"
Now I know: it's 67!

Guess 7: "Is it 67?" → "YES!" ✅

Only 7 guesses for 100 numbers!
```

---

## Binary Search Implementation

### Version 1: Iterative (Recommended)

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Find middle index
        mid = (left + right) // 2
        
        # Check if we found it
        if arr[mid] == target:
            return mid
        
        # Target is in right half
        elif arr[mid] < target:
            left = mid + 1  # Eliminate left half
        
        # Target is in left half
        else:
            right = mid - 1  # Eliminate right half
    
    return -1  # Not found

# Test it!
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
print(binary_search(arr, 23))  # Output: 5
print(binary_search(arr, 100)) # Output: -1 (not found)
```

### Let's Trace Through An Example

```python
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
target = 23

Iteration 1:
left = 0, right = 10
mid = (0 + 10) // 2 = 5
arr[5] = 23 ← FOUND! Return 5 ✅

# That was lucky! Let's try finding 67:

arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
target = 67

Iteration 1:
left = 0, right = 10
mid = (0 + 10) // 2 = 5
arr[5] = 23
23 < 67 → go right
left = 6, right = 10

Iteration 2:
mid = (6 + 10) // 2 = 8
arr[8] = 56
56 < 67 → go right
left = 9, right = 10

Iteration 3:
mid = (9 + 10) // 2 = 9
arr[9] = 67 ← FOUND! Return 9 ✅
```

---

### Version 2: Recursive (More Elegant)

```python
def binary_search_recursive(arr, target, left, right):
    # Base case: element not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Found it!
    if arr[mid] == target:
        return mid
    
    # Search right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    
    # Search left half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Usage:
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
result = binary_search_recursive(arr, 23, 0, len(arr) - 1)
print(result)  # 5
```

---

## Why is Binary Search O(log n)?

```python
# Each iteration cuts the problem in half

Array size: 100
After 1 comparison: 50 elements left
After 2 comparisons: 25 elements left
After 3 comparisons: 12 elements left
After 4 comparisons: 6 elements left
After 5 comparisons: 3 elements left
After 6 comparisons: 1 element left
After 7 comparisons: Found it! (or not found)

# Formula: How many times can you divide n by 2 until you get 1?
# That's log₂(n)

n = 100 → log₂(100) ≈ 7 comparisons
n = 1,000 → log₂(1,000) ≈ 10 comparisons
n = 1,000,000 → log₂(1,000,000) ≈ 20 comparisons

# Compare to linear search:
Linear search on 1,000,000 elements → 1,000,000 comparisons
Binary search on 1,000,000 elements → 20 comparisons
That's 50,000x faster! 🚀
```

---

## Common Binary Search Variations

### 1. Find First Occurrence
```python
def find_first(arr, target):
    """Find leftmost occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid      # Found one, but keep searching left
            right = mid - 1   # Look for earlier occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

arr = [1, 2, 2, 2, 2, 3, 4, 5]
print(find_first(arr, 2))  # Output: 1 (first index of 2)
```

### 2. Find Last Occurrence
```python
def find_last(arr, target):
    """Find rightmost occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid      # Found one, but keep searching right
            left = mid + 1    # Look for later occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

arr = [1, 2, 2, 2, 2, 3, 4, 5]
print(find_last(arr, 2))  # Output: 4 (last index of 2)
```

---

## Practice Problems

### Problem 1: Basic Binary Search
```python
# Implement binary search to find target in arr
# Return the index if found, -1 if not found

def binary_search(arr, target):
    # YOUR CODE HERE
    pass

# Test cases:
assert binary_search([1, 3, 5, 7, 9], 5) == 2
assert binary_search([1, 3, 5, 7, 9], 10) == -1
assert binary_search([1], 1) == 0
```

### Problem 2: Search Insert Position (LeetCode #35)
```python
# Given a sorted array and a target, return the index 
# where target would be inserted to keep array sorted

def search_insert(arr, target):
    # YOUR CODE HERE
    pass

# Test cases:
assert search_insert([1, 3, 5, 6], 5) == 2
assert search_insert([1, 3, 5, 6], 2) == 1
assert search_insert([1, 3, 5, 6], 7) == 4
assert search_insert([1, 3, 5, 6], 0) == 0
```

### Problem 3: First Bad Version
```python
# You are a product manager and currently leading a team to develop 
# a new product. Unfortunately, the latest version failed the quality 
# check. Since each version is developed based on the previous version, 
# all the versions after a bad version are also bad.
# Find the first bad version.

def is_bad_version(version):
    # This is provided by the system
    pass

def first_bad_version(n):
    # n versions: 1, 2, 3, ..., n
    # Use binary search to find first bad version
    # YOUR CODE HERE
    pass
```

---

## Solutions

<details>
<summary>Click to reveal solutions</summary>

```python
# Solution 1: Basic Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Solution 2: Search Insert Position
def search_insert(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # If not found, left is the insert position
    return left

# Solution 3: First Bad Version
def first_bad_version(n):
    left, right = 1, n
    
    while left < right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            right = mid  # Could be first bad, search left
        else:
            left = mid + 1  # Not bad, search right
    
    return left
```
</details>

---

## Key Takeaways

1. **Big O** measures how algorithm performance scales with input size
2. **Arrays** give O(1) access but O(n) insertion/deletion
3. **Binary Search** is O(log n) but requires **sorted** data
4. **Binary Search** eliminates half the search space each step

---