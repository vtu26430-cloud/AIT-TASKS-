def graph_coloring(graph):
    n = len(graph)
    result = [-1] * n    # color assignment for each node
    available = [False] * n  # track used colors

    # Assign color 0 to first node
    result[0] = 0

    # Assign colors to remaining nodes
    for u in range(1, n):
        # mark colors used by neighbors
        for neighbor in graph[u]:
            if result[neighbor] != -1:
                available[result[neighbor]] = True

        # find the first available color
        color = 0
        while color < n and available[color]:
            color += 1

        result[u] = color

        # reset the availability array for next iteration
        for neighbor in graph[u]:
            if result[neighbor] != -1:
                available[result[neighbor]] = False

    return result

# Example Run
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4, 5],
    4: [3, 5],
    5: [3, 4]
}

color_assignment = graph_coloring(graph)
print("Zone color assignment:", color_assignment)
