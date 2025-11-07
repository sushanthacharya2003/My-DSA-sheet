from typing import List

"""
Problem Description:
Design an algorithm to encode a list of strings to a single string and decode it back to the original list of strings.
There should be no restriction on what characters can be in the strings.

Key Requirements:
1. The encoding should be unique - different lists should produce different encodings
2. The decoding should perfectly reconstruct the original list
3. The algorithm should handle empty strings and special characters
4. The encoded string should be efficiently decodable

Solution Approach:
1. Encoding:
   - For each string, prepend its length followed by a delimiter (#)
   - This creates a format: <length>#<string> for each string
   - Concatenate all encoded strings together

2. Decoding:
   - Parse the string from left to right
   - At each step:
     a. Read digits until hitting '#' to get the length
     b. Extract the string of that length after the '#'
     c. Move pointer to the start of next length

Time Complexity:
- Encode: O(n), where n is total length of all strings
- Decode: O(n), where n is length of encoded string

Space Complexity:
- O(n) for both encode and decode

Test Cases:
1. Basic case:
   Input: ["hello", "world"]
   Encoded: "5#hello5#world"

2. Empty strings:
   Input: ["", ""]
   Encoded: "0#0#"

3. Special characters:
   Input: ["#", "##"]
   Encoded: "1##2###"

4. Mixed lengths:
   Input: ["a", "ab", "abc"]
   Encoded: "1#a2#ab3#abc"
"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            word = s[j:j + length]
            res.append(word)
            i = j + length
        return res

# Test cases
def test_encode_decode():
    solution = Solution()

    # Test case 1: Basic case with normal strings
    test1 = ["hello", "world"]
    encoded1 = solution.encode(test1)
    assert encoded1 == "5#hello5#world", f"Test 1 encode failed. Expected '5#hello5#world', got '{encoded1}'"
    decoded1 = solution.decode(encoded1)
    assert decoded1 == test1, f"Test 1 decode failed. Expected {test1}, got {decoded1}"
    print("Test case 1 passed!")

    # Test case 2: Empty strings
    test2 = ["", ""]
    encoded2 = solution.encode(test2)
    assert encoded2 == "0#0#", f"Test 2 encode failed. Expected '0#0#', got '{encoded2}'"
    decoded2 = solution.decode(encoded2)
    assert decoded2 == test2, f"Test 2 decode failed. Expected {test2}, got {decoded2}"
    print("Test case 2 passed!")

    # Test case 3: Special characters
    test3 = ["#", "##"]
    encoded3 = solution.encode(test3)
    assert encoded3 == "1##2###", f"Test 3 encode failed. Expected '1##2###', got '{encoded3}'"
    decoded3 = solution.decode(encoded3)
    assert decoded3 == test3, f"Test 3 decode failed. Expected {test3}, got {decoded3}"
    print("Test case 3 passed!")

    # Test case 4: Mixed length strings
    test4 = ["a", "ab", "abc"]
    encoded4 = solution.encode(test4)
    assert encoded4 == "1#a2#ab3#abc", f"Test 4 encode failed. Expected '1#a2#ab3#abc', got '{encoded4}'"
    decoded4 = solution.decode(encoded4)
    assert decoded4 == test4, f"Test 4 decode failed. Expected {test4}, got {decoded4}"
    print("Test case 4 passed!")

    # Test case 5: Unicode characters
    test5 = ["🌟", "hello世界"]
    encoded5 = solution.encode(test5)
    decoded5 = solution.decode(encoded5)
    assert decoded5 == test5, f"Test 5 decode failed. Expected {test5}, got {decoded5}"
    print("Test case 5 passed!")

if __name__ == "__main__":
    test_encode_decode()

