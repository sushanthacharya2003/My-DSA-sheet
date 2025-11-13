# 📝 **Problem Description — LeetCode 78: Subsets**

You’re given an array `nums` of **distinct integers**.
Your task:

> Return *all possible subsets* (also called the power set).

A subset can be:

* empty
* one element
* multiple elements
* full array
  Order of subsets doesn’t matter.

**Example**

```
Input:  nums = [1,2,3]
Output: 
[
  [], 
  [1], [2], [3],
  [1,2], [1,3], [2,3],
  [1,2,3]
]
```

There are **2ⁿ subsets** for an array of size **n**.

---

# 🧪 **Test Cases**

### ✅ Test Case 1

```
Input: [1,2,3]
Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
```

### ❕ Test Case 2 (Single element)

```
Input: [5]
Output: [[],[5]]
```

### ❕ Test Case 3 (Two elements)

```
Input: [0,1]
Output: [[],[0],[1],[0,1]]
```

### ❕ Test Case 4 (Empty input)

```
Input: []
Output: [[]]
```

### ❕ Test Case 5 (Negative numbers)

```
Input: [-1, -2]
Output: [[], [-1], [-2], [-1,-2]]
```

---

# 🧠 **Steps to Solve (Backtracking)**

This is the simplest and most intuitive approach.

### Step 1:

Start with an empty list `path = []`.

### Step 2:

Define a recursive function that accepts an index.

### Step 3:

If index reaches end → you have a complete subset → add it to result.

### Step 4:

Otherwise, for every element at `index`:

1. **Exclude** it → don’t add to path, go to next index
2. **Include** it → add to path, go to next index

   * after recursion, `pop()` to undo

### Step 5:

Recursion explores all YES/NO decisions for every element.

---

# 🧮 **Final Code (Backtracking)**

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(i):
            if i == len(nums):
                result.append(path[:])
                return

            # EXCLUDE nums[i]
            backtrack(i + 1)

            # INCLUDE nums[i]
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

        backtrack(0)
        return result
```

---

# ⏱️ **Time & Space Complexity**

### **Time Complexity: O(n × 2ⁿ)**

Why?

* There are `2ⁿ` subsets.
* Each subset costs up to `O(n)` to copy into the result.

### **Space Complexity: O(n)**

* `path` holds at most `n` elements
* recursion depth = `n`
* result storage takes `O(n × 2ⁿ)` but that’s output size, not algorithm overhead

---

# 🎤 **DSA Interview Questions & Answers Based on This Problem**

### **1️⃣ Why does subsets have 2ⁿ results?**

Each element has two choices:

* include
* exclude
  So total combinations:

```
2 × 2 × ... (n times) = 2ⁿ
```

---

### **2️⃣ Why is backtracking the preferred method?**

Because:

* It naturally models include/exclude decisions
* It explores all combinations without unnecessary computation
* Code stays clean and structured
* Works best when n ≤ 15 (typical constraints)

---

### **3️⃣ Could you solve this without recursion?**

Yes:

1. **Iterative method**:

   ```
   start with [[]]
   for each num:
       add num to all existing subsets
   ```
2. **Bitmask method** (0 to 2ⁿ - 1)

---

### **4️⃣ What’s the difference between combinations, subsets, and permutations?**

* **Subsets**: Order doesn’t matter, include/exclude
* **Combinations**: Order doesn’t matter, choose k items
* **Permutations**: Order matters

---

### **5️⃣ What happens if input contains duplicates?**

You must use a modified version (**Subsets II**) that:

* sorts array
* skips duplicates in recursion

---

### **6️⃣ Why do we use `path[:]`?**

Because if we append `path` directly, all stored subsets would reference the same list.
Using `path[:]` creates a *copy*.

---

### **7️⃣ What is the role of `path.pop()`?**

To **undo** the last choice.
This is what makes it *backtracking*:

```
choose → explore → un-choose
```

---
