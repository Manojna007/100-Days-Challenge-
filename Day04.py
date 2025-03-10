class BinaryTree:
    """Class representing a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ---------------- BRANCH SUM FUNCTION ----------------
def branchSums(root):
    """
    Computes the sum of all branches (root-to-leaf paths) in a binary tree.

    Args:
        root (BinaryTree): The root of the binary tree.

    Returns:
        List[int]: A list containing the sum of each root-to-leaf path.
    """
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

# 0(n) time | O(n) space
def calculateBranchSums(node, runningSum, sums):
    """
    Helper function to compute branch sums recursively.

    Args:
        node (BinaryTree): The current node.
        runningSum (int): The sum accumulated so far.
        sums (List[int]): The list storing all branch sums.
    """
    if node is None:
        return

    newRunningSum = runningSum + node.value  # Update running sum

    # If the node is a leaf, store the sum
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    # Recursively compute for left and right subtrees
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)


# ---------------- TEST CASE ----------------
if __name__ == "__main__":
    # Constructing a sample Binary Tree
    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.left.left = BinaryTree(2)
    root.left.left.left = BinaryTree(1)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(15)
    root.right.right = BinaryTree(22)

    print("Branch Sums:", branchSums(root))  # Output: [18, 20, 47]

    """
        Visual Representation of the Tree:

                10
               /  \
             5     15
            / \      \
           2   5      22
          /
         1

        Expected branch sums:
        - 10 -> 5 -> 2 -> 1  = 18
        - 10 -> 5 -> 5       = 20
        - 10 -> 15 -> 22     = 47
        """