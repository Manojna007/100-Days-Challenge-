class BinaryTree:
    """Class representing a node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Iterative Approach: O(n) time | O(h) space
def nodeDepths(root):
    """
    Computes the sum of all node depths in a binary tree using an iterative approach.

    Args:
        root (BinaryTree): The root of the binary tree.

    Returns:
        int: The sum of all node depths.
    """
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]  # Stack to track nodes and their depths

    while len(stack) > 0:
        nodeInfo = stack.pop()  # Pop the last added node
        node, depth = nodeInfo["node"], nodeInfo["depth"]

        if node is None:
            continue  # Skip if the node is None

        sumOfDepths += depth  # Add depth to total sum

        # Push left and right children with incremented depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sumOfDepths

# Recursive Approach: O(n) time | O(h) space
def nodeDepthsRecursive(root, depth=0):
    """
    Computes the sum of all node depths in a binary tree using recursion.

    Args:
        root (BinaryTree): The root of the binary tree.
        depth (int): The depth of the current node (default is 0).

    Returns:
        int: The sum of all node depths.
    """
    if root is None:
        return 0  # Base case: return 0 if node is None

    return depth + nodeDepthsRecursive(root.left, depth + 1) + nodeDepthsRecursive(root.right, depth + 1)

# ---------------- TEST CASE ----------------
if __name__ == "__main__":
    """
    Visual Representation of the Tree:

            10
           /  \
         5     15
        / \      \
       2   5      22
      /
     1

    
    """

    # Constructing a sample Binary Tree
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.right = BinaryTree(15)
    root.left.left = BinaryTree(2)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(22)
    root.left.left.left = BinaryTree(1)

    print("Node Depth Sum (Iterative):", nodeDepths(root))
    print("Node Depth Sum (Recursive):", nodeDepthsRecursive(root))