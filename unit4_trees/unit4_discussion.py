"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None  # empty BST

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # smaller goes left and larger goes right, allowing a search
        # to get rid of half a tree
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)

        if value < node.value:  # smaller nodes placed left
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:  # larger nodes placed right
            node.right = self._insert_recursive(node.right, value)
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST is more efficient as comparison allows us to eliminate a large
        # chunk of options via continuing left or right instead of checking
        # every value
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # if empty - value is not present
        if node is None:
            return False
        # value found at current node
        if value == node.value:
            return True
        # smaller value placed left
        if value < node.value:
            return self._search_recursive(node.left, value)
        # larger value is placed in the right
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # the output is sorted based on node size
        # every smaller value is left and every larger
        # is right. The left subtree is all smaller than current
        # node and the right subtree is all larger

        # smaller values first, larger last
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    tree = BST()
    values_to_insert = [70, 30, 10, 35, 55, 75, 105]

    print("Values inserted:", values_to_insert)

    # search space is reduced as there's no need to search
    # branches where the value wouldn't be. A smaller value
    # does not need to search right and larger not left.
    for value in values_to_insert:
        tree.insert(value)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")
    # the first value is root and everything after gets sorted
    # sorted output is: left = smaller and right = bigger
    sorted_values = tree.inorder()
    print("in-order traversal:", sorted_values)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")
    search_values = [30, 50, 70, 105, 15, 1]
    # searching for 70 would go right as 70 > 30 and 70 would be returned
    # searching for 80 would go right but return not found as it does not exist
    # searching for 15 would go left as 15 < 30 and 30 would be returned
    for value in search_values:
        if tree.search(value):
            print(f"Search for {value}: Found")
        else:
            print(f"Search for {value}: Not Found")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")
    empty_tree = BST()

    # traverse empty tree - returns []
    print("in-order traversal of empty tree:", empty_tree.inorder())

    # search empty tree - returns false
    print("Search for 1 in an empty tree:", empty_tree.search(1))

    tree.insert(30)  # insert duplicate value
    # the duplicate was ignored
    print("Traversal after duplicate value inserted:", tree.inorder())

    # tree with only one node
    single_node_tree = BST()
    single_node_tree.insert(1)
    # prints [1] as that's the only node in the tree
    print("Single-node tree traversal:", single_node_tree.inorder())


if __name__ == "__main__":
    main()
