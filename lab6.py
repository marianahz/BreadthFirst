from edgegraph import *
from collections import deque


def bfs(graph: GraphEL, start: VertexEL) -> list:
    if graph is None or start is None or start not in graph.vertices():
        return []

    visited = []
    bfs_order = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            bfs_order.append(vertex)
            for neighbor in graph.adjacent_vertices(vertex):
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order
