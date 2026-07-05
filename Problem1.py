## Problem 1 https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # LOGIC:
        # We use a Breadth-First Search (BFS) approach to traverse the tree level by level.
        # By keeping track of the `size` of the queue at the start of each iteration, 
        # we can process all nodes in the current row together and find the maximum value.
        #
        # TIME COMPLEXITY: $O(N)$
        # Where N is the total number of nodes in the tree. We visit and process every node exactly once.
        #
        # SPACE COMPLEXITY: $O(W)$ or $O(N)$
        # Where W is the maximum width of the tree. The queue stores nodes for one level at a time. 
        # In the worst case (a perfect binary tree), the bottom level will hold roughly N/2 nodes, 
        # which simplifies to $O(N)$ space.
        
        # Base case: if the tree is empty, return an empty list
        if not root:
            return []

        # Initialize a double-ended queue for BFS and append the root node
        q = collections.deque()
        q.append(root)

        # This array will store the largest value found in each row
        result = []

        # Continue traversing as long as there are nodes to process
        while q:
            # num of nodes in the current level
            size = len(q)
            # Track the maximum value for the current level, initialized to negative infinity
            maxForLevel = float('-inf')

            # Iterate strictly over the nodes in the current level
            for _ in range(size):
                # Pop the next node from the left of the queue
                element = q.popleft()
                # Update our max value if the current node's value is greater
                maxForLevel = max(element.val, maxForLevel)

                # If children exist, queue them up to be processed in the next level
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)

            # After checking all nodes in the current level, record the maximum value
            result.append(maxForLevel)

        return result