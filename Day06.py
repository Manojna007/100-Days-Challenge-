class Node:
    """Class representing a node in a directed graph (tree structure)."""

    def __init__(self, name):
        self.children = []  # List to store child nodes
        self.name = name  # Node name

    def addChild(self, name):
        """Adds a child node with the given name."""
        self.children.append(Node(name))

    # O(v + e) time | O(v) space
    def depthFirstSearch(self, array):
        """
        Performs Depth-First Search (DFS) traversal on the graph.
        DFS is a graph traversal algorithm that explores as far as possible
        along each branch before backtracking.

        Args:
            array (List[str]): List to store the DFS traversal order.

        Returns:
            List[str]: The DFS traversal order of nodes.
        """
        array.append(self.name)  # Add current node to traversal result
        for child in self.children:  # Recur for each child node
            child.depthFirstSearch(array)
        return array


# ---------------- TEST CASE ----------------
if __name__ == "__main__":
    """
    Graph Structure (Tree Representation):

           A
         / | \
        B  C  D
       / \   / \
      E   F G   H

    Expected DFS Output: ["A", "B", "E", "F", "C", "D", "G", "H"]
    """

    root = Node("A")  # Root node
    root.addChild("B")
    root.addChild("C")
    root.addChild("D")

    root.children[0].addChild("E")  # B -> E
    root.children[0].addChild("F")  # B -> F
    root.children[2].addChild("G")  # D -> G
    root.children[2].addChild("H")  # D -> H

    print("DFS Traversal:", root.depthFirstSearch([]))
    # Output: ["A", "B", "E", "F", "C", "D", "G", "H"]