
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

FOUND = "FOUND"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"


def dls(node, goal, limit, path):

    if node == goal:
        return FOUND, path
    if len(path) - 1 == limit:
        if any(child not in path for child in graph.get(node, [])):
            return CUTOFF, None
        return FAILURE, None
    cutoff_seen = False
    for child in graph.get(node, []):

        if child in path:
            continue
        status, result_path = dls(
            child, goal, limit, path + [child]
        )
        if status == FOUND:
            return FOUND, result_path

        if status == CUTOFF:
            cutoff_seen = True
    if cutoff_seen:
        return CUTOFF, None
    return FAILURE, None
def iddfs(start, goal, max_depth):
    attempts = []
    for limit in range(max_depth + 1):
        status, path = dls(start, goal, limit, [start])
        attempts.append((limit, status, path))
        if status == FOUND:
            return status, path, attempts
        if status == FAILURE:
            return status, None, attempts
    return CUTOFF, None, attempts
print("DLS RESULTS")

for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit, ["A"])
    print("Limit:", limit, "| Status:", status, "| Path:", path)
print("\nIDDFS RESULTS")
for maximum in [1, 2, 3, 4]:
    status, path, attempts = iddfs("A", "G", maximum)
    print("Maximum depth:", maximum)
    print("Status:", status)
    print("Path:", path)
    print("Limits attempted:", [item[0] for item in attempts])
    print()
