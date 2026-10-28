
import heapq
from collections import deque

weighted_graph = {
    "A": [("B", 1), ("C", 5)],
    "B": [("D", 4), ("E", 1)],
    "C": [("F", 2), ("G", 7)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}

def ucs(start, goal):
    frontier = [(0, start, [start])]
    best_cost = {start: 0}
    processing_order = []

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        if cost != best_cost.get(node):
            continue

        processing_order.append(node)

        if node == goal:
            return path, cost, processing_order

        for neighbor, edge_cost in weighted_graph[node]:
            new_cost = cost + edge_cost

            if new_cost < best_cost.get(
                neighbor, float("inf")
            ):
                best_cost[neighbor] = new_cost

                heapq.heappush(
                    frontier,
                    (new_cost, neighbor, path + [neighbor])
                )

    return None, float("inf"), processing_order

def bfs(start, goal):
    queue = deque([(start, [start])])
    seen = {start}

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        for neighbor, edge_cost in weighted_graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None
def path_cost(path):
    if path is None:
        return float("inf")

    total = 0

    for u, v in zip(path, path[1:]):
        for neighbor, cost in weighted_graph[u]:
            if neighbor == v:
                total += cost
                break

    return total


ucs_path, ucs_cost, order = ucs("A", "G")

print("UCS Path:", ucs_path)
print("UCS Total Cost:", ucs_cost)
print("UCS Processing Order:", order)

bfs_path = bfs("A", "G")
print("\nBFS Path:", bfs_path)
print("BFS Total Cost:", path_cost(bfs_path))
