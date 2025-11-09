# LeetCode 347. Top K Frequent Elements
# -------------------------------------
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - k is in the range [1, the number of unique elements in nums]
# - It is guaranteed that the answer is unique.
#
# Follow up: What if you want the top k frequent elements sorted by frequency?
#
# Algorithm (Heap/Bucket Sort):
# 1. Count the frequency of each element using a hashmap.
# 2. Use a heap or bucket sort to efficiently find the k most frequent elements.
# 3. Return the result.
#
# Steps:
# - Build a frequency map.
# - Use a heap (min-heap of size k) or bucket sort to extract top k frequent elements.
# - Return the result list.
#
# Optimal Solution (Heap):
import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

# Inbuilt test cases
if __name__ == "__main__":
    nums1 = [1,1,1,2,2,3]
    k1 = 2
    print("Test 1:", topKFrequent(nums1, k1))  # Output: [1,2]
    nums2 = [1]
    k2 = 1
    print("Test 2:", topKFrequent(nums2, k2))  # Output: [1]

# Time Complexity: O(N log k) where N is the length of nums
# Space Complexity: O(N)

"""
DSA Interview Questions & Answers
---------------------------------
Q1: How do you efficiently find the k most frequent elements in an array?
A1: Use a hashmap to count frequencies, then a heap or bucket sort to extract the k most frequent.

Q2: Why is a heap preferred over sorting for this problem?
A2: A heap allows us to keep track of the k largest frequencies in O(N log k) time, which is faster than sorting all elements (O(N log N)).

Q3: Can you solve this problem in linear time?
A3: Yes, using bucket sort. After counting frequencies, place elements into buckets indexed by frequency, then collect the k most frequent from the buckets.

Q4: What are the trade-offs between heap and bucket sort approaches?
A4: Heap is easier to implement and works well for small k. Bucket sort is optimal for large N and k, but requires extra space for buckets.
"""
import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result
#time complexity: O(N log k)
#space complexity: O(N)



"""
1: Why use a heap instead of sorting the entire array for Top K Frequent Elements?
A1 (Key Insight):

"Sorting would take O(n log n) time, but a min-heap of size k lets us maintain only the top k elements in O(n log k) time. For large n and small k (e.g., k=10), this is significantly faster. Example: If k=10 and n=1M, we avoid sorting 1M elements."
Why it matters: Shows you optimize for real-world constraints (k is usually small).

Q2: How would you handle ties in frequency (e.g., two elements with same count)?
A2 (Critical Detail):

"The problem doesn’t specify tie-breaking rules, so I’d clarify with the interviewer. In practice, we’d use the element itself as a secondary sort key (e.g., lexicographical order) to ensure deterministic output. For example, if freq(3)=freq(5)=2, return [3,5] or [5,3] based on the problem’s expected behavior."
Why it matters: Tests your attention to edge cases and communication skills.

Q3: What if k = n (all elements are top k)?
A3 (Edge Case Analysis):

"If k = n, the solution reduces to returning all elements. Using a heap would be inefficient (O(n log n)), so we’d skip the heap and just return all keys from the frequency map. This is a good spot to mention: 'We should check for trivial cases early to optimize runtime.'"
Why it matters: Proves you think beyond the "standard" solution.

Q4: How does the bucket sort approach work here, and when is it better than a heap?
A4 (Alternative Solution Insight):

"Bucket sort uses an array where index = frequency. We place each element in the bucket at its frequency index. Then we iterate from highest frequency down to 1 to collect top k elements. This is O(n) time (no sorting/heap), but uses O(n) extra space. It’s ideal when frequencies are small (e.g., k << n) or when n is known to be manageable."
Why it matters: Shows you know multiple approaches and their trade-offs.

Why these questions?
Q1 separates candidates who understand complexity beyond "heap is faster."
Q2 reveals if you handle ambiguity (a real interview skill).
Q3 tests edge-case awareness.
Q4 proves you can compare algorithms, not just implement one.
"""
