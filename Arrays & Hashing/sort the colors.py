
# LeetCode 75. Sort Colors
# -----------------------
# Given an array nums with n objects colored
# red, white, or blue, sort them in-place so
# that objects of the same color are adjacent,
# with the colors in the order red, white, and
# blue. We will use the integers 0, 1, and 2
# to represent the color red, white, and blue,
# respectively.
#
# You must solve this problem without using
# the library's sort function.
#
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
# Constraints:
# - n == nums.length
# - 1 <= n <= 300
# - nums[i] is either 0, 1, or 2.
#
# Follow up: Could you come up with a one-pass
# algorithm using only constant extra space?

"""
Optimal Solution: Dutch National Flag
Algorithm
-----------------------------------
Explanation:
We use three pointers: low, mid, and high.
- low: the next position for 0
- mid: the current element
- high: the next position for 2
We iterate through the array and swap elements
to their correct positions in a single pass.

Steps:
1. Initialize low = 0, mid = 0, high = n - 1
2. While mid <= high:
     - If nums[mid] == 0: swap with nums[low],
         increment low and mid
     - If nums[mid] == 1: just increment mid
     - If nums[mid] == 2: swap with nums[high],
         decrement high

Time Complexity: O(n) (single pass)
Space Complexity: O(1) (in-place)
"""

def sortColors(nums):
    """Sorts the array in-place using Dutch
    National Flag algorithm."""
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Inbuilt test case
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print("Original:", nums)
    sortColors(nums)
    print("Sorted:", nums)  # Output: [0, 0, 1, 1, 2, 2]
	sortColors(nums)
	print("Sorted:", nums)  # Output: [0, 0, 1, 1, 2, 2]

"""
INTERVIEW Q&A
Ah! You want it **like an actual DSA interview**, Q\&A style, not just an explanation. Got it. Here’s a set of likely questions an interviewer might ask on **Sort Colors (Leetcode 75)**, with concise, precise answers.

---

### **1. Q: Can you explain the problem in your own words?**

**A:** We are given an array containing only `0`, `1`, and `2`. We need to sort it **in-place** such that all `0`s come first, followed by `1`s, then `2`s. The challenge is to do this in **one pass** using **constant space**.

---

### **2. Q: How would you approach it initially?**

**A:** The naive approach is to count the number of 0s, 1s, and 2s, and overwrite the array. But that’s two passes (count + overwrite). The optimal is **Dutch National Flag Algorithm** using three pointers (`low`, `mid`, `high`) to sort in a single pass.

---

### **3. Q: What is the Dutch National Flag Algorithm?**

**A:**

1. Maintain three pointers:

   * `low` → next position for 0
   * `mid` → current element
   * `high` → next position for 2
2. Traverse the array with `mid`:

   * If `nums[mid] == 0`, swap with `low` and increment `low` & `mid`
   * If `nums[mid] == 1`, just increment `mid`
   * If `nums[mid] == 2`, swap with `high` and decrement `high`
3. Stop when `mid > high`.

This sorts in **one pass, O(n) time, O(1) space**.

---

### **4. Q: Can you write the code?**

**A: Python code:**

```python
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
```

---

### **5. Q: What is the time and space complexity?**

**A:**

* **Time Complexity:** O(n) — each element is visited at most once.
* **Space Complexity:** O(1) — in-place swaps, no extra array.

---

### **6. Q: What edge cases should be tested?**

**A:**

1. Empty array: `[]` → returns `[]`
2. Single element: `[0]`, `[1]`, `[2]` → unchanged
3. Already sorted: `[0,0,1,1,2,2]` → unchanged
4. Reverse sorted: `[2,2,1,1,0,0]` → becomes `[0,0,1,1,2,2]`
5. Only one type: `[0,0,0]` → unchanged

---

### **7. Q: Can this be solved in two passes?**

**A:** Yes, using **counting sort**: count 0s, 1s, and 2s, then overwrite the array.

* **Time Complexity:** O(n)
* **Space Complexity:** O(1) (if counts stored in 3 variables)
* **Drawback:** Two passes instead of one.

---

### **8. Q: Why is Dutch National Flag considered optimal?**

**A:**

1. Single pass → O(n)
2. In-place → O(1) space
3. Elegant → uses pointers without extra storage
4. Handles edge cases naturally

---

If you want, I can make a **full 15–20 Q\&A set** covering **every tricky follow-up an interviewer can ask** on this problem. That’s usually what gets you the real “DSA interview ready” prep.

Do you want me to do that?

"""

