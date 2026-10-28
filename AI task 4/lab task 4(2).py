
import heapq

def search(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    processed = []
    expanded = 0

    while pq:
        priority, cost, node, path = heapq.heappop(pq)

        if cost != best[node]:
            continue

        processed.append(node)

        if node == goal:
            return path, cost, processed, expanded

        expanded += 1

        for nxt, weight in graph.get(node, []):
            new_cost = cost + weight

            if new_cost < best.get(nxt, float("inf")):
                best[nxt] = new_cost
                heapq.heappush(
                    pq,
                    (new_cost + h[nxt], new_cost,
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

heuristic = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}
zero_h = {node: 0 for node in graph}

print("A* Search Result:")
print(search(graph, heuristic, "S", "G"))
print("\nUCS Search Result:")
print(search(graph, zero_h, "S", "G"))
