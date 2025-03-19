"""
Problem Statement:
Given a sorted array and a target value, implement Binary Search to find the target's index.
If the target is not found, return -1.

Binary Search works by:
1. Checking the middle element of the array.
2. If it matches the target, return its index.
3. If the target is smaller, search the left half (recursively or iteratively).
4. If the target is larger, search the right half.

Binary Search is **O(log(n))** in time complexity since it halves the search space at each step.
"""

# -------------------- APPROACH 1: RECURSIVE BINARY SEARCH --------------------
# O(log(n)) Time | O(log(n)) Space (due to recursive calls)
def binarySearchRecursive(array, target):
    """
    Performs binary search recursively.
    :param array: Sorted list of integers.
    :param target: Integer value to search for.
    :return: Index of the target if found, else -1.
    """
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1  # Target not found

    middle = (left + right) // 2
    potentialMatch = array[middle]

    if target == potentialMatch:
        return middle  # Target found at index `middle`
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)  # Search left half
    else:
        return binarySearchHelper(array, target, middle + 1, right)  # Search right half


# -------------------- APPROACH 2: ITERATIVE BINARY SEARCH --------------------
# O(log(n)) Time | O(1) Space
def binarySearchIterative(array, target):
    """
    Performs binary search iteratively.
    :param array: Sorted list of integers.
    :param target: Integer value to search for.
    :return: Index of the target if found, else -1.
    """
    left, right = 0, len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]

        if target == potentialMatch:
            return middle  # Target found
        elif target < potentialMatch:
            right = middle - 1  # Move left
        else:
            left = middle + 1  # Move right

    return -1  # Target not found


# -------------------- TEST CASE --------------------
if __name__ == "__main__":
    test_array = [1, 3, 5, 7, 9, 11, 13]
    target = 7

    print("Recursive Binary Search Index:", binarySearchRecursive(test_array, target))
    print("Iterative Binary Search Index:", binarySearchIterative(test_array, target))