def bfs(graph, start, end):
  """
  Performs a breadth-first search of the given graph, starting at the given node.

  Args:
    graph: The graph to search.
    start: The node to start the search from.
    end: The node to find.

  Returns:
    True if there is a path from start to end, False otherwise.
  """

  visited = set()
  queue = [(start, 0)]

  while queue:
    node, depth = queue.pop(0)

    if node == end:
      return True

    visited.add(node)

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append((neighbor, depth + 1))

  return False
