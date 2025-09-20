"""
PROBLEM 202: Happy Number
============================
Given a number n, repeatedly replace n with the sum of the squares of its digits until n becomes 1 (where it will stay), or it loops endlessly in a cycle that does not include 1. Return true if n ends in 1, and false if it loops endlessly.
Example 1:
Input: n = 19
Output: true
Explanation: 1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:
Input: n = 2
Output: false

"""
class Solution:
    def sum_of_squares(self,n): 
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sum_of_squares(n)
        while fast != 1 and slow != fast:
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(self.sum_of_squares(fast))
        return fast == 1
        
    
    """
    Approach 2 : HashSet
    def isHappy_set(n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
        return n == 1
    """
# Time Complexity: O(log n) where n is the input number
# Space Complexity: O(1)    
# Approach: Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
# Inbuilt input example
if __name__ == "__main__":  
    n = 19  # You can change this input for other test cases
    sol = Solution()
    print(sol.isHappy(n))
#output: True
"""
STEPS:
🛠️ Approaches to Solve

Here are two common methods:

1. Hash Set / Seen Numbers Approach

Maintain a set of numbers you've already seen in the process.

Each iteration: compute next = sum of squares of digits of current n.

If next == 1, return True.

If next is in the set already, you have a loop → return False.

This detects cycles by remembering past states. 
LeetCodee
+1

2. Floyd’s Cycle-Finding Algorithm (Slow & Fast Pointers)

Use two “pointers” or values: slow and fast.

slow moves one step at a time (i.e. compute the next once).

fast moves two steps at a time (compute next twice).

If at any point fast == 1, you’ve reached happiness → return True.

If slow == fast (and not 1), there's a cycle → return False.

This avoids needing extra space for storing all seen values. 
Jaywin
+2
LeetCodee
+2
"""
"""
1️⃣ What is a Happy Number?

Q: Can you define a happy number?
A:
A happy number is a positive integer that eventually reaches 1 when you repeatedly replace the number with the sum of the squares of its digits. If it falls into a cycle that does not include 1, the number is not happy.

Example: 19 → 82 → 68 → 100 → 1 → Happy.

Example: 2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → Cycle, not happy.

2️⃣ How would you solve the problem?

Q: What’s the brute-force approach?
A:

Keep computing the sum of squares of digits.

Store each intermediate result in a set.

If we see 1, return True.

If we see a number already in the set, we’ve hit a cycle → return False.

Time Complexity: O(k·log n), where k = number of iterations until repetition.

Space Complexity: O(k) (due to set).

3️⃣ Can you optimize the space?

Q: How can you detect cycles without using extra space?
A:

Use Floyd’s Cycle Detection (tortoise and hare):

Have two pointers (slow and fast).

slow moves one step at a time.

fast moves two steps at a time.

If fast == 1 → happy number.

If slow == fast (and not 1) → cycle, not happy.

Time Complexity: O(k·log n)

Space Complexity: O(1)

4️⃣ Why does the algorithm always terminate?

Q: How do you know the process doesn’t run infinitely with new numbers?
A:

Any number eventually reduces to a number ≤ 243 because the maximum sum of squares for a 32-bit integer (999...9 with 10 digits) is 10 * 9² = 810.

Once below 243, there are only finitely many states → either we reach 1 or enter a cycle.

5️⃣ Can you dry-run with an example?

Q: Show how the algorithm works for n = 19.
A:

Slow = 19, Fast = sum_of_squares(19) = 82

Next: Slow = 82, Fast = sum_of_squares(sum_of_squares(82)) = sum_of_squares(68) = 100

Next: Slow = 68, Fast = sum_of_squares(sum_of_squares(100)) = sum_of_squares(1) = 1

Fast reached 1 → 19 is happy.

6️⃣ What concepts does this test?

A:

Mathematical modeling: Turning number into digit-based transformations.

Hashing / cycle detection: Using a set OR Floyd’s algorithm.

Optimization trade-offs: Space vs Time.

Problem reasoning: Why cycles are guaranteed.

7️⃣ Possible Variants in Interview

Find all happy numbers in range [1…N].

Return the cycle (not just True/False).

Generalize to sum of k-th powers of digits (e.g., cubes).

👉 Would you like me to also prepare a ready-to-speak 3–4 min interview script answer (like if the interviewer directly asks “Explain the Happy Number problem and how you’d solve it”)?

"""