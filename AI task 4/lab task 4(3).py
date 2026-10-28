
import heapq

def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    processed = []
    expanded = 0

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best[node]:
            continue

        processed.append(node)

        if node == goal:
            return path, g, processed, expanded

        expanded += 1

        for nxt, weight in graph.get(node, []):
            new_g = g + weight

            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                heapq.heappush(
                    pq,
                    (new_g + h[nxt], new_g,
                     nxt, path + [nxt])
                )

    return None, float("inf"), processed, expanded


graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}


original_h = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}

overestimate_h = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 10,
    "G": 0
}
print("Original A* Result:")
print(astar(graph, original_h, "S", "G"))
print("\nModified A* Result:")
print(astar(graph, overestimate_h, "S", "G"))
