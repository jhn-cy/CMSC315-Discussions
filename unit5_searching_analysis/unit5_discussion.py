"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # linear search checks every item in the list once in the worst case,
    # so time complexity is 0(n), where n is the list length
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            left = middle + 1
            # the target can only be to the right of middle
            # removes the left half of the remaining search space
        else:
            right = middle - 1
            # the target can only be to the left of middle
            # removes the right half of the remaining search space
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")
    small_dataset = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    existing = 7
    non_existing = 6
    print("dataset:", small_dataset)

    # should return index 3
    print("Searching for a value that exists:", existing)
    print("Linear search test:", linear_search(small_dataset, existing))
    print("Binary search test:", binary_search(small_dataset, existing))

    # should return -1
    print("Searching for a value that doesn't exist:", non_existing)
    print("Linear search test:", linear_search(small_dataset, non_existing))
    print("Binary search test:", binary_search(small_dataset, non_existing))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")
    # creates sorted list from 0 through 2999999
    large_dataset = list(range(3000000))

    # BST are more efficient as datasets grow larger because it cuts remaining range in half
    # with target values being in the beginning, it might not matter much, but if the target is at the end,
    # it would significantly cut down on search time as the dataset gets larget as it doesn not need to search each entry
    large_existing = 299
    large_non = 30000001
    print("Searching for a value that exists:", large_existing)
    print("Linear search test:", linear_search(large_dataset, large_existing))
    print("Binary search test:", binary_search(large_dataset, large_existing))

    print("Searching for a value that doesn't exist:", large_non)
    print("Linear search test:", linear_search(large_dataset, large_non))
    print("Binary search test:", binary_search(large_dataset, large_non))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    # edge case 1: a one-item list
    # searching for the only item in the list will return index 0 as it is the only item
    one_item_list = [3]
    print("One item list:", one_item_list)
    print("Linear search:", linear_search(one_item_list, 3))
    print("Binar search:", binary_search(one_item_list, 3))

    # edge case 2: a value at the last position
    # the search will return the last index
    print("Dataset we are searching:", small_dataset)
    print("Linear search for 21:", linear_search(small_dataset, 21))
    print("Binar search for 21:", binary_search(small_dataset, 21))

    # edge case 3: an empty list
    # the search will return a -1 as there is nothing in the list to search
    empty_list = []
    print("Empty list:", empty_list)
    print("Linear search for 7 in an empty list:", linear_search(empty_list, 7))
    print("Binar search for 7 in an empty list:", binary_search(empty_list, 7))


if __name__ == "__main__":
    main()
