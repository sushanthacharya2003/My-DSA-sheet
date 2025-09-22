"""
LeetCode 572. Subtree of Another Tree
-------------------------------------
Given the roots of two binary trees root and subRoot, return True if there is a subtree of root with the same structure and node values as subRoot and False otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: True

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: False

Constraints:
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= Node.val <= 10^4

Explanation & Steps:
--------------------
1. Traverse the main tree (root) and for each node, check if the subtree starting at that node matches subRoot.
2. To check if two trees are the same, compare their root values and recursively check their left and right subtrees.
3. If any subtree of root matches subRoot, return True; otherwise, return False.

Approach:
- Use recursion to traverse root and compare subtrees using a helper function.
- Time Complexity: O(m * n) in the worst case (m = nodes in root, n = nodes in subRoot).
- Space Complexity: O(max(m, n)) for recursion stack.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # ...existing code...
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if self.isSame(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSame(self,a,b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val!=b.val:
            return False
        return self.isSame(a.left,b.left) and self.isSame(a.right,b.right)


# Inbuilt test case
def build_tree_from_list(vals):
    """Helper to build a binary tree from a list (LeetCode style)."""
    if not vals:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    # Example 1:
    root_list = [3,4,5,1,2]
    subroot_list = [4,1,2]
    root = build_tree_from_list(root_list)
    subroot = build_tree_from_list(subroot_list)
    sol = Solution()
    print("Is subRoot a subtree of root?", sol.isSubtree(root, subroot))  # Output: True
    
    
    """interview-style questions spun off from the Subtree of Another Tree problem, and give you answers you’d be expected to produce.

Q1. Identical Trees

Question:
Given two binary trees, write a function to check if they are identical (same structure + values).

Answer (Idea):

If both nodes are None → return True.

If only one is None → return False.

If values differ → return False.

Otherwise check left and right recursively.

Code (Python):

def isSame(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False
    return isSame(a.left, b.left) and isSame(a.right, b.right)


Complexity:

Time: O(min(m, n)) if m,n are sizes of trees.

Space: O(h) recursion depth, h = height of smaller tree.

✅ Interviewer happy if you write this cleanly.

Q2. Subtree Count

Question:
Instead of checking if subRoot is a subtree, count how many times it appears inside root.

Answer (Idea):

Traverse every node in root.

Each time you find a node that matches subRoot (using isSame), increment count.

Return final count.

Code (Python):

def countSubtrees(root, subRoot):
    if not root:
        return 0
    count = 0
    if isSame(root, subRoot):
        count += 1
    count += countSubtrees(root.left, subRoot)
    count += countSubtrees(root.right, subRoot)
    return count


Complexity:

Worst case O(m·n), same as isSubtree.

But this version counts all matches instead of returning early.

✅ Shows you can extend logic beyond yes/no.

Q3. Optimized Subtree Check

Question:
The naive solution is O(m·n). Can you make it faster?

Answer (Idea):

Serialize both trees (preorder with null markers).

Check if serialized string of subRoot is a substring of root’s serialization.

Use KMP (linear-time substring search) or Rabin–Karp (hashing) to avoid O(m·n).

Code (Python-ish):

def serialize(root):
    if not root:
        return "X"   # null marker
    return f"#{root.val} {serialize(root.left)} {serialize(root.right)}"

def isSubtree(root, subRoot):
    s1 = serialize(root)
    s2 = serialize(subRoot)
    return s2 in s1   # substring check (can optimize with KMP)


Example Serialization:
Tree [4,1,2] → #4 #1 X X #2 X X
Tree [4,1,2] is clearly inside [#3 #4 #1 X X #2 X X #5 X X].

Complexity:

Serialization: O(m + n).

Substring check: O(m + n) with KMP.

Much better than O(m·n).

✅ Interviewer wants to see you think beyond brute force.

⚡️ Bonus Tip: After solving Q3, the interviewer might say:
"Cool, but what if the trees are so deep that recursion causes stack overflow?"
Safe answer: implement serialization iteratively using a stack.

Do you want me to expand this into a 10-question interview prep sheet (with answers) just based on this subtree theme, so you can drill them one by one?
    """