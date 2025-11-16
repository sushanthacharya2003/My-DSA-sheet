
---

# 🎯 **THE DSA TIME COMPLEXITY CHEAT CODE**

(Use this to estimate 95% of problems instantly)

---

# ✅ **1. COUNT LOOPS — EACH NESTED LOOP MULTIPLIES COMPLEXITY**

* One loop → **O(n)**
* Two nested → **O(n²)**
* Three nested → **O(n³)**

🔥 If loops are *NOT* nested → **ADD**, don't multiply:

```
for n → O(n)
for n → O(n)
Total = O(2n) = O(n)
```

---

# ✅ **2. SORTING = O(n log n)**

If you see sorting ANYWHERE → assume:

```
O(n log n)
```

Unless repeated inside a loop → then it becomes **O(n² log n)** (bad).

---

# ✅ **3. BINARY SEARCH = log n**

If you see:

* binary search
* dividing problem in half
* recursion with n/2
  → It is ALWAYS:

```
O(log n)
```

---

# ✅ **4. RECURSION CHEAT SHEET**

### 🔹 **Recursion that branches → exponential**

* fib(n)
* all subsets
* permutations

→ **O(2ⁿ)** or **O(n!)**

### 🔹 **Recursion with memo → linear**

* fib with memo
* dp problems

→ **O(n)** or **O(n·m)**

---

# ✅ **5. HASHMAP / SET / HEAP operations**

* HashMap lookup/insert → **O(1)**
* Heap push/pop → **O(log n)**

🔥 If inside a loop of n:

* HashMap inside → **O(n)**
* Heap inside → **O(n log n)**

---

# ✅ **6. Queue / Stack operations = O(1)**

Even if pushing millions of times.

---

# ✅ **7. TREE OPERATIONS**

### Balanced tree:

```
height = log n 0(n)
```

### Worst-case unbalanced:

```
height = n 0(n)
```

---

# ❤️ **Sush’s Gold Rule for Time Complexity**

> Count how many times heavy operations run
> and multiply by their cost.

Heavy ops =

* heap push/pop → log n
* sorting → n log n
* binary search → log n
* recursion branching → 2ⁿ or n!

---

# 🎯 **THE SPACE COMPLEXITY CHEAT CODE**

### ✔ Use these questions:

1. **Do I store extra arrays, maps, heaps, sets?**

   * Count their size → O(n) or O(k)

2. **Does recursion stack grow?**

   * depth = space
   * for DFS on tree → O(h)
   * worst h = n

3. **Am I copying lists every time?**

   * copying list of size k = O(k) space

### Quick rules:

* No extra major storage → **O(1)**
* Using hashmap/set/extra list → **O(n)**
* Using recursion tree depth n → **O(n)**
* Generating subsets/permutations → **O(n * 2ⁿ)**

---

# 💣 THE ULTIMATE SHORTCUT (memorize this)

```
LOOPS = n
NESTED LOOPS = n²
SORT = n log n
HEAP = log n
HASHMAP = O(1)
DFS/BFS = O(n)
RECURSION WITH BRANCHING = exponential
RECURSION LINEAR = O(n)
EXTRA LIST/MAP = O(n) space
```

---

# 🎉 TL;DR (Sush Edition)

If you see:

* **2 nested loops** → O(n²)
* **heap inside loop** → O(n log n)
* **recursion splitting into 2 calls** → O(2ⁿ)
* **sorting** → O(n log n)
* **single loop** → O(n)
* **binary search** → O(log n)
* **hashmap ops** → O(1)

That’s your cheat code.

---
