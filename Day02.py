"""
   Problem Description:
   Given two arrays: `array` and `sequence`, check if `sequence` is a subsequence of `array`.
   A sequence is a subsequence if all its elements appear in `array` in the same order,
   but they do not have to be consecutive.

   Example:
   array = [5, 1, 22, 25, 6, -1, 8, 10]
   sequence = [1, 6, -1, 10]
   Output: True (because [1, 6, -1, 10] appears in the same order in `array`)

   Constraints:
   - Elements in `sequence` must appear in `array` in the same order.
   - The function should return `True` if `sequence` is a subsequence of `array`, else `False`.
   """


def validateSubsequence_while(array, sequence):
    """
    Check if 'sequence' is a subsequence of 'array' using a while loop.
    """
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1  # Move sequence pointer if a match is found
        arrIdx += 1  # Always move array pointer

    return seqIdx == len(sequence)  # True if all sequence elements are found


def validateSubsequence_for(array, sequence):
    """
    Check if 'sequence' is a subsequence of 'array' using a for loop.
    """
    seqIdx = 0  # Pointer for sequence

    for num in array:
        if seqIdx == len(sequence):  # If sequence is fully matched, stop early
            break
        if num == sequence[seqIdx]:  # Match found, move sequence pointer
            seqIdx += 1

    return seqIdx == len(sequence)  # True if all elements in sequence are matched


# Example Test Cases
array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, 10]
sequence2 = [1, 10, 6]

print(validateSubsequence_while(array1, sequence1))  # Output: True
print(validateSubsequence_while(array1, sequence2))  # Output: False

print(validateSubsequence_for(array1, sequence1))    # Output: True
print(validateSubsequence_for(array1, sequence2))    # Output: False