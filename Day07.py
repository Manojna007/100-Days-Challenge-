class Node:
    """Represents a node in a doubly linked list."""
    def __init__(self, value):
        self.value = value
        self.prev = None  # Points to the previous node
        self.next = None  # Points to the next node


class DoublyLinkedList:
    """Implementation of a Doubly Linked List (DLL)."""
    def __init__(self):
        self.head = None  # First node of the DLL
        self.tail = None  # Last node of the DLL

    def setHead(self, node):
        """Sets the given node as the head of the list."""
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        """Sets the given node as the tail of the list."""
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        """Inserts nodeToInsert before the given node."""
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        """Inserts nodeToInsert after the given node."""
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        """Inserts nodeToInsert at the given position (1-based index)."""
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        """Removes all nodes with the specified value."""
        node = self.head
        while node is not None:
            nextNode = node.next
            if node.value == value:
                self.remove(node)
            node = nextNode

    def remove(self, node):
        """Removes a specific node from the list."""
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self._removeBindings(node)

    def _removeBindings(self, node):
        """Helper method to remove node bindings from DLL."""
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        """Checks if a node with the given value exists in the list."""
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

    def printList(self):
        """Prints the list from head to tail."""
        node = self.head
        result = []
        while node is not None:
            result.append(str(node.value))
            node = node.next
        print(" <-> ".join(result))


# ---------------- TEST CASE ----------------
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Creating nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    # Setting head and tail
    dll.setHead(node1)
    dll.setTail(node5)

    # Inserting nodes
    dll.insertAfter(node1, node2)  # 1 <-> 2 <-> 5
    dll.insertAfter(node2, node3)  # 1 <-> 2 <-> 3 <-> 5
    dll.insertBefore(node5, node4)  # 1 <-> 2 <-> 3 <-> 4 <-> 5

    print("Doubly Linked List after insertions:")
    dll.printList()  # Expected: 1 <-> 2 <-> 3 <-> 4 <-> 5

    # Removing a node
    dll.remove(node3)  # Removes node with value 3
    print("\nDoubly Linked List after removing 3:")
    dll.printList()  # Expected: 1 <-> 2 <-> 4 <-> 5

    # Checking for a value
    print("\nContains 4?", dll.containsNodeWithValue(4))  # Expected: True
    print("Contains 3?", dll.containsNodeWithValue(3))  # Expected: False

    # Removing all nodes with a specific value
    dll.removeNodesWithValue(2)
    print("\nDoubly Linked List after removing all 2s:")
    dll.printList()  # Expected: 1 <-> 4 <-> 5