"""Explore a small undirected graph using only Python's standard library."""

from collections import deque


def breadth_first_search(graph: dict[str, list[str]], start: str) -> list[str]:
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def main() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"],
    }

    print("Graph theory: a first example")
    print(f"Vertices: {len(graph)}")
    print(f"Edges: {sum(len(neighbors) for neighbors in graph.values()) // 2}")
    print("Vertex degrees:")
    for vertex, neighbors in graph.items():
        print(f"  {vertex}: {len(neighbors)}")
    print(f"Breadth-first traversal from A: {' -> '.join(breadth_first_search(graph, 'A'))}")


if __name__ == "__main__":
    main()
