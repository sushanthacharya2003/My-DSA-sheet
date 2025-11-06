# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0   # keeps track of the maximum diameter found

        def height(node):
            if not node:
                return 0
            # Get height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Update diameter at this node
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return height of this subtree
            return 1 + max(left_height, right_height)

        height(root)  # start DFS
        return self.max_diameter



LeetCode 543 (Diameter of Binary Tree) in an interview, they won’t just stop at “code it.” They’ll probe around. Here are the DSA interview-style Q&A that can spin off directly from this problem:

1. What is the diameter of a binary tree?

👉 Answer:

Diameter = the number of edges in the longest path between any two nodes.

This path may or may not pass through the root.

Example: In a skewed tree of 4 nodes, diameter = 3 (the path includes all edges).

2. How is diameter different from height?

👉 Answer:

Height: longest path from root to a leaf.

Diameter: longest path between any two nodes.

Height must pass through root, diameter doesn’t have to.

3. What is the time complexity of your solution?

👉 Answer:

Efficient solution = O(n), because we compute height and update diameter in one DFS traversal.

Naïve solution = O(n²) if we calculate height separately at each node.

4. What is the space complexity?

👉 Answer:

O(h), where h = height of the tree (recursion stack).

Best case (balanced tree): O(log n).

Worst case (skewed tree): O(n).

5. Does the longest path (diameter) always pass through the root?

👉 Answer:

No. Example:

      1
       \
        2
       / \
      3   4


Longest path is 3 → 2 → 4 (2 edges), doesn’t include root (1).

6. How would you modify the solution if the problem asked for the number of nodes in the longest path (instead of edges)?

👉 Answer:

Just return self.max_diameter + 1 (since nodes = edges + 1).

7. Can you solve it iteratively (without recursion)?

👉 Answer:

Yes, using postorder traversal with a stack to compute heights, or by simulating recursion.

But recursive DFS is simpler and usually accepted in interviews unless constraints are huge.

8. How does this compare to BFS? Could we use BFS?

👉 Answer:

Yes, using BFS you can find longest path in a tree by doing:

BFS from any node to find farthest node A.

BFS from A to find farthest node B.

Distance(A,B) = diameter.

This works since tree has no cycles.

9. Trick Question: What is the diameter of an empty tree? What about a single-node tree?

👉 Answer:

Empty tree = 0.

Single node = 0 (no edges).

10. Follow-up: What if the tree is weighted (edges have weights)?

👉 Answer:

Instead of just counting edges, you’d compute left_weight + right_weight at each node.

Or use BFS twice with weights considered (Dijkstra for general graphs, but since tree has no cycles, DFS works fine).

⚡ If you want, I can also give you a list of variations interviewers ask after this, like “find the longest path sum instead of diameter” or “find k-th longest path”.

Want me to prep you for those variants too?
