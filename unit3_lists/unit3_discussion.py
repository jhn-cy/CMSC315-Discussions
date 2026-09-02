"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # after an insertion occurs, existing elements (at the inserted index and to the right) are shifted one position to the right
    lst.insert(index, value) # insertion performance depends on where the insertion is (beginning is slower as more elements need to shift)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # validates the index before removing - preventing IndexError with invalid indexes / empty lists
    if 0 <= index < len(lst):
        return lst.pop(index) # return removed value
    return None # if index is invalid


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Python checks items one at a time (linear search) from the first to the last (sequentially)
    for index in range(len(lst)):
        if lst[index] == value:
            return index # if value is found
    return -1 # if value is not found


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")
    student_courses = [115, 215, 315] # creates a list of student course numbers. 3 items in list
    print("Original List: ",student_courses)
    insert_at(student_courses, 0, 410) # inserts at beginning (list shifts right). 4 items in list
    print("After inserting 410 at beginning: ", student_courses)
    insert_at(student_courses, 2, 600) # Insert in middle, all items from insertion (2) to the right shift right. 5 items in list
    print("After inserting 600 in middle: ",student_courses)
    insert_at(student_courses, 5, 310) # inserts at end (no items shift). 6 items in list
    print("After inserting 310 at end: ", student_courses)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    print("Current List:", student_courses) # current list
    remove_beginning = delete_at(student_courses, 0) # remove the first item (all values shift left)
    print("Remove from beginning: ", remove_beginning)
    print("Changed List:", student_courses)

    middle_index = len(student_courses) // 2 # remove the middle item (all values to the right shift left)
    remove_middle = delete_at(student_courses, middle_index)
    print("Remove from the middle: ", remove_middle)
    print("Changed List: ", student_courses)

    remove_end = delete_at(student_courses, len(student_courses) - 1) # remove the final item. No items shift
    print("Removed from the end:", remove_end)
    print("Changed List:", student_courses)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    print("Current List:", student_courses)
    # searching for course in the list
    existing_course = 315
    existing_result = search_value(student_courses, existing_course)
    if existing_result != -1:
        print(f"Student Course {existing_course} found at index {existing_result}.")
    else:
        print(f"Student Course {existing_course} not found.")

    # searching for course not in the list
    missing_course = 0
    missing_result = search_value(student_courses, missing_course)
    if missing_result != -1:
        print(f"Student Course {missing_course} was found at index {missing_result}.")
    else:
        print(f"Student ID {missing_course} not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")
    invalid = delete_at(student_courses, -1)
    invalid2 = delete_at(student_courses, 300)
    print("Delete at index -1 and 300 (invalid)?: ", invalid, invalid2)
    print("Current List:", student_courses)

    empty_list = []
    insert_at(empty_list, 0, "Inserting into empty list works")
    print("After inserting into an empty list:", empty_list)

    empty_delete = delete_at([], 0)
    print("Attempt to delete from empty list: ", empty_delete)

    search_and_destroy = search_value([], "Item")
    print("Search for missing value:", search_and_destroy)


if __name__ == "__main__":
    main()
