"""
LeetCode 268. Missing Number
---------------------------
Given an array nums containing n distinct
numbers in the range [0, n], return the only
number in the range that is missing from the
array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers,
so all numbers are in the range [0,3]. 2 is the
missing number in the range since it does not
appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers,
so all numbers are in the range [0,2]. 2 is the
missing number in the range since it does not
appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers,
so all numbers are in the range [0,9]. 8 is the
missing number in the range since it does not
appear in nums.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

Follow up: Could you implement a solution using
only O(1) extra space complexity and O(n) runtime
complexity?
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        xorfull=0
        for i in range(n+1):
            xorfull^=i
        xorarray=0
        for j in nums:
            xorarray^=j
        return xorfull ^ xorarray


# Inbuilt input example
if __name__ == "__main__":
    nums = [3, 0, 1]  # You can change this input for other test cases
    sol = Solution()

    print(sol.missingNumber(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
#APPROACH: Using XOR (Bit Manipulation)
"""
============================
DSA INTERVIEW QUESTIONS ON
'MISSING NUMBER'
============================

Q1: How would you approach finding the
missing number in an array containing n
distinct numbers in the range [0, n]?
Describe multiple approaches.
A1:
1. Using Summation:
    - Calculate sum from 0 to n: n*(n+1)//2
    - Subtract sum(nums) from this value to
      get the missing number.
2. Using XOR (Bit Manipulation):
    - XOR all numbers from 0 to n and all
      numbers in nums. The result is the
      missing number.
3. Using a Hash Set (or Boolean Array):
    - Add all nums to a set, then check for
      the first number in 0..n not in the set.

Q2: Implement the most efficient solution
for finding the missing number. What are
its time and space complexities?
A2:
Both Summation and XOR approaches are O(n)
time and O(1) space. See code above for XOR.
Summation version:

     class Solution:
          def missingNumber(self, nums: list[int]) -> int:
                n = len(nums)
                return n * (n + 1) // 2 - sum(nums)

Q3: What are the advantages and disadvantages
of the Summation and XOR approaches?
A3:
Summation: Intuitive, but can overflow in some
languages. XOR: No overflow, but less intuitive.

Q4: What if the numbers were in the range [1, n]
instead of [0, n], and one number was missing?
How would you adapt your solutions?
A4:
Just change the range in summation/XOR from 1 to n
instead of 0 to n.

Q5: What if there were two missing numbers instead
of one, and the range was [0, n]?
A5:
Use sum and sum of squares to form two equations,
or use XOR and partition by a set bit to find both
missing numbers.

COMMENT THIS AT LAST AS DSA INTERVIEW QUESTIONS
ASKED ON THIS TOPIC
"""

