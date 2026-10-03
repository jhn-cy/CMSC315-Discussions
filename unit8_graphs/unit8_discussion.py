"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    if start not in graph:
        return []
    visited = {start}
    order = []
    queue = deque([start])

    while queue:
        current = queue.popleft()
        order.append(current)
        # a queue is used because it processes nodes in the order they were added
        # BFS visits all nodes at one level before the next
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # each node - a place in a small neighboorhood
    # each edge - a road between two nodes

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")
    graph = {
        "Home": ["School", "Pool"],
        "School": ["Home", "Library", "Park"],
        "Pool": ["Home", "Park"],
        "Library": ["School", "Disco"],
        "Park": ["School", "Pool"],
        "Disco": ["Library"],
    }
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")
    # BFS visits Home then it's neighbors then nodes farther away
    start = "Home"
    print(f"Starting at {start}: {bfs(graph, start)}")
    # add one additional node or edge
    graph["Funeral"] = ["Park"]
    graph["Disco"].append("Funeral")

    # demonstrate updated traversal
    print("Graph after adding Funeral:")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    print(f"Updated traversal from {start}: {bfs(graph, start)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    # starting from a different node - changes traversal's starting point
    print(f"Starting at Library: {bfs(graph, 'Library')}")
    # handle a missing start node safely - return an empty list
    print(f"Missing node: {bfs(graph, 'Party')}")


if __name__ == "__main__":
    main()

