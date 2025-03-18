"""
Problem Statement:
Given a "special" array containing integers and nested arrays, return its "product sum."
The product sum is calculated by multiplying each element by its depth in the array.

Rules:
- Regular integers contribute normally.
- Nested arrays contribute their sum multiplied by their depth.

Example:
Input: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Output: 12
Explanation:
5 + 2 + (2 * (7 + (-1))) + 3 + (2 * (6 + (3 * (-13 + 8)) + 4)) = 12

Approach:
1. Use recursion to process each element.
2. If an element is a nested list, recursively call `productSum` with an increased multiplier.
3. If an element is an integer, add it to the sum.
4. Multiply the final sum by the depth multiplier.
"""

# -------------------- FUNCTION IMPLEMENTATION --------------------
# O(n) Time Complexity | O(d) Space Complexity
def productSum(array, multiplier=1):
    """
    Recursively calculates the product sum of a special array.
    :param array: List containing integers and nested lists.
    :param multiplier: Current depth multiplier (default is 1).
    :return: Integer representing the product sum.
    """
    total = 0
    for element in array:
        if isinstance(element, list):
            total += productSum(element, multiplier + 1)  # Increase multiplier for nested lists
        else:
            total += element  # Regular numbers are added directly
    return total * multiplier  # Multiply by depth before returning


# -------------------- TEST CASE --------------------
if __name__ == "__main__":
    test_array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    print("Product Sum:", productSum(test_array))