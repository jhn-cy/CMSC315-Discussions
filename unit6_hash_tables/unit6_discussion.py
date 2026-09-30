"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    age = {}
    # a dictionary (like a hash table) stores data as key-value pairs

    age["James"] = 21
    age["Monica"] = 33
    age["Andrew"] = 24
    age["John"] = 41
    age["Valerie"] = 31

    print("Dictionary contents:", age)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")
    # the lookup works via dictionary keys (that are hashed by Python) used to find the associated value
    # the key here is the name and the age is the value
    valerie_age = age["Valerie"]
    john_age = age["John"]

    print("Lookup results (Valerie): ", valerie_age)
    print("Lookup results (John): ", john_age)
    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")
    # when an existing key is assigned a new value, the value that is already stored gets updated
    # to the new value
    print("Dictionary before: ", age)
    print("Updating John from 41 to 42")
    age["John"] = 42
    print("Dictionary after: ", age)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")
    # When a key is removed, the entire key-value pair is removed and
    # the key can no longer be used to retrieve the value
    print("Dictionary before deletion: ", age)
    print("Deleting James, Monica, and Andrew from the dictionary.")
    del age["James"], age["Monica"], age["Andrew"]
    print("Dictionary after deletion: ", age)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case: delete a missing key safely
    # Using pop(key, default) returns the default value so no KeyError
    # gets raised when Jerry is not found because it is a missing key
    print()
    print("Edge Case 1:")
    removed_key = age.pop("Jerry", "No Entry Removed")
    print("Deleting Jerry:", removed_key)
    print("After safely disposing:", age)
    print()

    # Edge case: update a missing key
    # Updating a missing key (assigning a value to it)
    # automatically adds that key-value pair, so now it exists
    print("Edge Case 2:")
    print("Updating a missing key (adding a new key-value pair)")
    print("Dictionary before:", age)
    age["Jerry"] = 33
    print("Dictionary after:", age)
    print()

    # Edge case: use an empty dictionary
    # There are no key-value pairs, but values can be added later on
    print("Edge Case 3:")
    empty_dictionary = {}
    print("Empty dictionary: ", empty_dictionary, ",Length: ", len(empty_dictionary))
    print()


if __name__ == "__main__":
    main()
