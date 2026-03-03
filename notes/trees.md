Great example. Let me walk you through how a D&C mind thinks about it step by step.

---

## Problem: Find the maximum number in an array

```python
arr = [3, 1, 7, 2, 9, 4]
```

---

### The Normal (Non D&C) Way of Thinking

Most beginners think: "Let me just loop through everything and track the biggest number I've seen."

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```

This works. But your brain approached it as **one big problem.**

---

### The D&C Way of Thinking

Ask yourself: **"What if I didn't have to solve the whole thing at once?"**

The thought process goes like this:

**Step 1 — Divide.** "What if I split the array into two halves?"
```
[3, 1, 7]    and    [2, 9, 4]
```

**Step 2 — Conquer.** "I'll find the max of each half separately. I don't care how yet — I'll just trust that it works."
```
max of [3, 1, 7]  →  7
max of [2, 9, 4]  →  9
```

**Step 3 — Combine.** "The overall max is just whichever of those two is bigger."
```
max(7, 9)  →  9  ✅
```

But wait — how did we find the max of each half? **Same way. Split again.**

```
[3, 1, 7]
    ↓
[3, 1]  and  [7]

[3, 1]
    ↓
[3]  and  [1]
```

Now each piece has **one element.** The max of a single element is just... itself. That's your **base case** — the point where the problem becomes so small it solves itself.

---

### The Full Code

```python
def find_max(arr, left, right):
    # Base case — one element, return it
    if left == right:
        return arr[left]

    # Divide — find the middle
    mid = (left + right) // 2

    # Conquer — find max of each half
    left_max  = find_max(arr, left, mid)
    right_max = find_max(arr, mid + 1, right)

    # Combine — return the bigger one
    return max(left_max, right_max)

arr = [3, 1, 7, 2, 9, 4]
print(find_max(arr, 0, len(arr) - 1))  # 9
```

---

### Visualizing the Splits

```
         [3, 1, 7, 2, 9, 4]
               /       \
        [3, 1, 7]     [2, 9, 4]
          /    \        /    \
       [3,1]  [7]    [2,9]  [4]
       /   \          /   \
      [3]  [1]      [2]   [9]

Combine back up:
max(3,1)=3   max(2,9)=9
max(3,7)=7   max(9,4)=9
    max(7, 9) = 9 ✅
```

---

### The Key Mindset Shift

The D&C thinker never asks *"how do I solve all of this?"* They ask **"how do I split this so that solving a smaller version gives me the answer to the bigger version?"**

Once you can answer that question, the rest follows naturally.

Make sense? Want me to give you a small one to try yourself before we move on?