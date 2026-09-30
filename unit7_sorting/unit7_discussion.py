"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # copy the list so original data is not changed
    sorted_list = lst.copy()
    # each pass moves the largest remaining value to the end
    for end in range(len(sorted_list) - 1, 0, -1):
        swapped = False
        # compare adjacent values in unsorted portion
        for index in range(end):
            if sorted_list[index] > sorted_list[index + 1]:
                sorted_list[index], sorted_list[index + 1] = (
                    sorted_list[index + 1],
                    sorted_list[index],
                )
                swapped = True
        # stop early if no swaps occurred
        if not swapped:
            break
    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # lists with 0 or 1 item are already sorted
    if len(lst) <= 1:
        return lst.copy()
    # divide list into smaller halves
    middle = len(lst) // 2
    right_half = lst[:middle]
    left_half = lst[middle:]

    # recursively sort both halves with merged results after
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    left_index = 0
    right_index = 0

    # add smaller next value from the two sorted lists
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # append remaining values
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")
    ds_1 = [17, -7, 3, 0, 23, 21, 14, 7, 12]
    bubble_1 = bubble_sort(ds_1)
    merge_1 = merge_sort(ds_1)
    print("Original list: ", ds_1)
    print("Bubble sort: ", bubble_1)
    print("Merge sort: ", merge_1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")
    ds_2 = [11, -3, 2, 1, 33, 24, 13, 9, 21]
    bubble_2 = bubble_sort(ds_2)
    merge_2 = merge_sort(ds_2)
    print("Original list: ", ds_2)
    print("Bubble sort: ", bubble_2)
    print("Merge sort: ", merge_2)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # no values - already sorted
    empty_list = []
    print("Original list: ", empty_list)
    print("Bubble sort: ", bubble_sort(empty_list))
    print("Merge sort: ", merge_sort(empty_list))

    # both algorithms return the same order.
    # bubble sort stops early due to no swaps
    already_sorted = [1, 3, 5, 7, 9, 11, 13]
    print("Original list: ", already_sorted)
    print("Bubble sort: ", bubble_sort(already_sorted))
    print("Merge sort: ", merge_sort(already_sorted))

    # repeated values are kept and sorted
    duplicate = [3, 2, 1, 1, 2, 3]
    print("Original list: ", duplicate)
    print("Bubble sort: ", bubble_sort(duplicate))
    print("Merge sort: ", merge_sort(duplicate))


if __name__ == "__main__":
    main()

