class BST:
    """
    Class representing a node in a Binary Search Tree (BST).
    Each node has a value, a left child, and a right child.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ---------------- PROBLEM DESCRIPTION ----------------
"""
Problem: Find the Closest Value in a Binary Search Tree (BST)

Given a BST and a target integer value, find the closest value to the target present in the BST.
The closest value is the node value that has the minimum absolute difference with the target.

### Example:
        10
       /  \
      5    15
     / \   /  \
    2   5 13  22
   /        \
  1          14

Input: BST root, target = 12  
Output: 13  
(13 is closest to 12 compared to other node values)

### Constraints:
- The tree follows BST properties: left subtree < root < right subtree.
- There will always be **at least one node** in the BST.
- The target can be any integer (not necessarily present in the BST).
- If multiple values have the same difference from the target, return any one of them.

### Complexity Analysis:
1. **Recursive Approach**
   - **Time Complexity:** O(log(n)) on average, O(n) in the worst case (skewed tree).
   - **Space Complexity:** O(log(n)) for recursion stack (O(n) in the worst case).

2. **Iterative Approach**
   - **Time Complexity:** O(log(n)) on average, O(n) in the worst case.
   - **Space Complexity:** O(1) since we use no extra space apart from variables.

Both approaches return the same correct result but differ in their use of recursion.
"""


# ---------------- RECURSIVE APPROACH ----------------
def findClosestValueInBst(tree, target):
    """
    Recursive function to find the closest value in a BST.
    Calls a helper function with an initial closest value set to infinity.
    """
    return findClosestValueInBstHelper(tree, target, float("inf"))


def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest  # Return the closest found when reaching a leaf node

    # Update closest if the current node is closer to target
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

        # Traverse left or right based on target value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest  # Exact match found


# ---------------- ITERATIVE APPROACH ----------------
def findClosestValueInBstIterative(tree, target):
    """
    Iterative function to find the closest value in a BST.
    Uses a while loop instead of recursion to reduce space complexity.
    """
    closest = float("inf")
    current_node = tree

    while current_node is not None:
        # Update closest if the current node is closer to target
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value

            # Move left or right based on comparison
        if target < current_node.value:
            current_node = current_node.left  # Move left
        elif target > current_node.value:
            current_node = current_node.right  # Move right
        else:
            break  # Found exact match, exit loop

    return closest


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    # Constructing a sample BST
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.right = BST(5)
    root.left.left.left = BST(1)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.right = BST(22)
    root.right.left.right = BST(14)

    # Test cases
    target = 12
    print("Recursive Approach:", findClosestValueInBst(root, target))  # Output: 13
    print("Iterative Approach:", findClosestValueInBstIterative(root, target))  # Output: 13

    target = 17
    print("Recursive Approach:", findClosestValueInBst(root, target))  # Output: 15
    print("Iterative Approach:", findClosestValueInBstIterative(root, target))  # Output: 15

    target = 23
    print("Recursive Approach:", findClosestValueInBst(root, target))  # Output: 22
    print("Iterative Approach:", findClosestValueInBstIterative(root, target))  # Output: 22