"""
Whenever there’s a requirement to find two data elements in an array that
satisfy a certain condition, the two pointers pattern should be the first
strategy to come to mind.
# Using two pointers can make the solution faster than using a nested loop,
form N^2 to O(N)

Yes,    if all of these conditions are fulfilled:
    The input data can be traversed in a linear fashion,
    that is, it’s in an array,
    in a linked list, or in a string of characters.

    We limit our focus to a specific range of elements within
     the input data, as dictated
    by the positions of the two pointers, allowing us to consider
     a small subset of elements
    rather than the entire set.


No, if either of these conditions is fulfilled:
    The input data cannot be traversed in a linear fashion, that is, it’s neither in an array, nor in
    a linked list, nor in a string of characters.
    The problem requires an exhaustive search of the solution space, that is, eliminating one solution
    does not eliminate any others.
"""

'''
Time complexity: O(N)
Run (n/2) times because of two pointers
Constant space complexity: O(1)

Problem 1:

Note: A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward.

# Simplify version
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left, right = left + 1, right - 1
    return True
'''


def is_palindrome(s: str) -> bool:
    # Remove any non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(ch for ch in s if ch.isalnum()).lower()

    # Initialize two pointers at the beginning and end of the string
    left, right = 0, len(clean_s) - 1

    # Continue comparing characters while the left pointer is less than the right pointer
    while left < right:
        if clean_s[left] != clean_s[right]:
            return False
        left += 1
        right -= 1

    return True


# Driver code
def main():
    test_cases = ["RACECAR", "ABBA", "TART"]
    i = 1
    for s in test_cases:
        print("Test Case #", i)
        print(is_palindrome(s))
        print("-" * 100, end="\n\n")
        i = i + 1


if __name__ == '__main__':
    main()
