

# ✅ **LeetCode 1046 — Last Stone Weight**

### **Problem Statement**

You’re given an array `stones` of positive integers.
Each turn:

1. Pick **two heaviest** stones.
2. Smash them.
3. If equal → both destroyed
4. If not equal → the heavier becomes `(heavier - lighter)` and goes back in the pile.

This continues until ≤ 1 stone remains.

Return the weight of the last stone, or **0** if none remain.

---

# ✅ **Test Cases**

### **Case 1**

```
Input:  [2,7,4,1,8,1]
Output: 1
```

### **Case 2**

```
Input:  [1]
Output: 1
```

### **Case 3**

```
Input:  [3,3]
Output: 0
```

### **Case 4**

```
Input:  [10, 9, 3, 2]
Output: 0
```

### **Case 5**

```
Input:  []
Output: 0
```

---

# ✅ **Dry Run (Example)**

Input:

```
[2,7,4,1,8,1]
```

Convert to max-heap using negatives:

```
[-8, -7, -4, -2, -1, -1]
```

**Step 1:**
Pop → `8` & `7` → diff = 1
Push `-1`

**Step 2:**
Pop → `4` & `2` → diff = 2
Push `-2`

**Step 3:**
Pop → `2` & `1` → diff = 1
Push `-1`

**Step 4:**
Pop → `1` & `1` → equal → both removed

Remaining: `[-1]` → answer = **1**

---

# ✅ **Why Heap?**

Because every move requires:

* Getting the largest two values
* Doing it fast

Heap:

* `pop` → O(log n)
* `push` → O(log n)

Total → **O(n log n)**

Sorting every time would be slow as hell.

---

# ✅ **Python Code (Correct + Clean)**

```python
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to negatives to simulate max-heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # Keep smashing until ≤ 1 stone left
        while len(stones) > 1:
            first = -heapq.heappop(stones)   # largest
            second = -heapq.heappop(stones)  # second largest

            if first > second:
                diff = first - second
                heapq.heappush(stones, -diff)

        return -stones[0] if stones else 0
```

This is the version interviewers expect.

---

# ✅ **Interview Questions Asked From This Problem**

### **1. Why use a max-heap and not sorting?**

Sorting every time → O(n² log n)
Heap operations → O(n log n)

### **2. Why negative numbers in Python?**

`heapq` is a **min-heap**, negatives flip it into a **max-heap**.

### **3. What is the time complexity?**

```
O(n log n)
```

### **4. Space complexity?**

```
O(n)
```

### **5. What edge cases should we handle?**

* Empty array
* One stone
* All equal
* Large values

### **6. Could you solve without heap?**

Yes → but slower
(sort + simulate → bad performance)

### **7. What if stone weights were bounded (e.g., ≤ 1000)?**

Then bucket sort or counting sort could work.

---
