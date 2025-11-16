"""
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

Example 1:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Explanation:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

Output: [null, 7, 7, 7, 8]

Explanation:

KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8
 

Constraints:

0 <= nums.length <= 104
1 <= k <= nums.length + 1
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add


"""


import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)

        # Keep only k largest elements
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)

        # If heap grows beyond k, pop the smallest
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        # Root is kth largest
        return self.minheap[0]
"""
Q1: Why do we use a MIN-heap instead of a MAX-heap?
Answer:

Because we want to efficiently track the kth LARGEST element.

A min-heap of size k keeps the k largest elements.

The smallest among them (root) = kth largest.

Max-heap would store the biggest at root — useless for O(1) kth largest.

🚀 Q2: Why do we keep the heap size exactly equal to k?
Answer:

Because if we store ONLY the top k largest values, then:

the smallest among them = kth largest

accessible instantly at heap[0]

If we kept all values → root wouldn't represent kth largest.

Heap size > k → pop smallest
Heap size == k → perfect

🚀 Q3: What is the time complexity of .add(val)?
Answer:
O(log k)


Because:

heappush → O(log k)

optionally heappop → O(log k)

Heap never grows beyond k.

🚀 Q4: What is the space complexity?
Answer:
O(k)


We store only k elements in the heap.

🚀 Q5: Why does .heapify(nums) take O(n) instead of O(n log n)?
Answer:

Because heapify builds a heap using a bottom-up approach.

Every level requires fewer operations, adding up to O(n).

This is a known result:

heapify = O(n)

🚀 Q6: Why do we pop the smallest element when heap size exceeds k?
Answer:

Because it’s not part of the top k largest elements.

Example: k = 3
Heap has: [8, 10, 12, 3]

3 is useless → pop it.

🚀 Q7: Can this be solved with sorting?
Answer:

Not efficiently.

Sorting for each add(val):

O(n log n)


Our heap approach:

O(log k)


Much faster for streaming data.

🚀 Q8: What happens if the incoming value is smaller than the kth largest?
Answer:

It still gets pushed — but then the smallest (maybe the same value) is popped.

Which means:
It will not affect the heap if it's not in the top k elements.

🚀 Q9: Why is kth largest available at heap[0]?
Answer:

Heap root always stores the smallest element in the heap.

Since heap contains k largest numbers,
the smallest among them = kth largest.

🚀 Q10: Can this solution handle negative numbers?
Answer:

Yes, heaps don’t care about sign.
Order comparisons work normally.

🚀 Q11: What if nums initially has fewer than k elements?
Answer:

Heap remains smaller until enough values are added.

Kth largest is only valid once heap reaches size k.

Some implementations return the largest until then, but LeetCode guarantees behavior.

🚀 Q12: Can we use a max-heap instead?
Answer (smart interviewer-friendly):

Only if we store n − k + 1 smallest elements,
but that reverses the logic and wastes space/time.

Min-heap of size k is optimal.

🚀 Q13: What data structure is the best for this problem?
Answer:
Min-heap (priority queue)


Why?

Supports fast insert

Maintains ordering

Keeps only top k elements

O(log k) updates

O(1) query

🚀 Q14: Is this approach optimal?
Answer:

Yes.

You cannot do better than O(log k) per insertion
because you must maintain sorted structure of top k elements.

🚀 Q15: How would you modify this to find Kth SMALLEST element in a stream?
Answer:

Use a max-heap of size k:

Keep k smallest elements

Root (max) = kth smallest

Same logic, reversed direction.

🎯 TL;DR (Sush Edition)

Your solution is a min-heap of size k.
Interviewers love asking:

why min-heap not max-heap

why heap size = k

why time = log k

how heapify = O(n)

how to extend to kth smallest or median







