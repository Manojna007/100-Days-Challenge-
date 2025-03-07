# Problem: Given an array of integers, return a pair of numbers that add up to a given target sum.
# Approach 1: Brute force approach with O(n^2) time complexity and O(1) space complexity.
# Approach 2: Hash map approach with O(n) time complexity and O(n) space complexity.
# Approach 3: Two-pointer approach with O(n log n) time complexity and O(1) space complexity.

# Approach 1: O(n^2) time | O(1) space (Brute Force)
def twoNumberSum_bruteforce(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


# Approach 2: O(n) time | O(n) space (Hash Map)
def twoNumberSum_hashmap(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


# Approach 3: O(n log n) time | O(1) space (Two-pointer)
def twoNumberSum_twopointer(array, targetSum):
    array.sort()  # Sorting the array first.
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


# Example usage:

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

print("Brute Force Approach (O(n^2) time | O(1) space):", twoNumberSum_bruteforce(array, targetSum))
print("Hash Map Approach (O(n) time | O(n) space):", twoNumberSum_hashmap(array, targetSum))
print("Two-pointer Approach (O(n log n) time | O(1) space):", twoNumberSum_twopointer(array, targetSum))