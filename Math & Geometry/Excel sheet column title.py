"""
168. Excel Sheet Column Title
Solved
Easy
Topics
premium lock icon
Companies
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
"""
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 0-based index
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Approach: Mathematical Conversion
# Inbuilt input example
if __name__ == "__main__":
    columnNumber = 701  # You can change this input for other test cases
    sol = Solution()
    print(sol.convertToTitle(columnNumber))

#output: ZY



"""
Steps to get the letters:

Subtract 1 from N. Now, N = 2001. Take N modulo 26 and convert the result to the corresponding position in the alphabet. 2001 % 26 = 25, which corresponds to Z, since we start with A = 0.
Divide N by 26. We have N= 
26
2001
​
 =76.
Repeat the process until N = 0. We subtract 1, so now N = 75. Take it modulo 26: 75 % 26 = 23. This corresponds to X.
Divide N by 26. We have N= 
26
75
​
 =2.
Subtract 1, so now N = 1. Take it modulo 26: 1 % 26 = 1. This corresponds to B.
Finally, we are done, because  
26
N
​
 =0. The result is BXZ, the reverse order in which we found the letters.

Algorithm
Initialize an empty string ans which would store the column title.

Do the following as long as columnNumber is greater than 0:

Subtract 1 from the columnNumber
Find the character corresponding to columnNumber % 26 and append it to the ans in the end.
Assign columnNumber to columnNumber / 26.
Reverse the string columnNumber and return it
Conceptual Q&A

Q1. What type of number system is this problem based on?

It’s similar to base-26, but with a twist → it’s a bijective base-26 system (no zero digit, digits go A=1 … Z=26).

Q2. Why do we subtract 1 from columnNumber before taking modulo?

Because Excel’s system is 1-indexed.

Without subtracting, numbers like 26 (Z) or 52 (AZ) get misaligned.

Example: 26 should map to 'Z'.

If we don’t subtract → 26 % 26 = 0 → 'A' → WRONG.

If we subtract first → (25 % 26) = 25 → 'Z' → ✅

Q3. Why do we reverse the result at the end?

Because when you repeatedly take remainders, you extract “digits” from least significant to most significant.

Example: 701 → "ZY" → we first get 'Y', then 'Z', so reversing is required.

Q4. What’s the time complexity of the solution?

Each iteration divides columnNumber by 26.

Complexity = O(log₍₂₆₎ columnNumber) (number of “digits”).

Space complexity = O(log₍₂₆₎ columnNumber) for result storage.

Q5. Can we solve this without reversing the string at the end?

Yes. If you build the string from the front using a stack/deque or insert at index 0 (result.insert(0, char)), you don’t need to reverse later.

But inserting at the start repeatedly is less efficient (O(n²)), so reversal is the better approach.

Q6. How is this related to other DSA problems?

It’s a variant of integer to string in arbitrary base conversion.

Shows up in problems like:

“Convert number to base-n string”

“Decode column title back to number” (the reverse problem, LeetCode #171).

Also conceptually linked to string encoding/decoding and bijective mappings.

🔹 Coding Q&A

Q7. What happens if you mistakenly use chr(remainder) instead of chr(ord('A')+remainder)?

You’ll get ASCII control characters ('\x00', '\x01'...) instead of letters.

Only correct mapping is chr(ord('A') + remainder) → gives 'A'..'Z'.

Q8. Why do we use "".join(result) instead of concatenating strings directly?

"".join(list) is O(n) efficient.

Repeated string concatenation (result += char) is O(n²) in Python, since strings are immutable.

Q9. Edge Case Test: What should convertToTitle(702) return?

702 → 'ZZ'

First remainder → 701 % 26 = 25 → Z

Then → 26 % 26 = 0 → Z after subtracting properly.

So final = "ZZ".

⚡ Pro Tip for Interviews: If asked this, also mention the reverse problem → Excel Column Number (LeetCode #171). Interviewers love when you connect both."""