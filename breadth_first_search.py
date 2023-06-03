from collections import deque

def bfs(graph, start):
  visited = set()     # Set to store visited vertices
  queue = deque()     # Queue to store vertices to be visited
  queue.append(start) # Enqueue the starting vertex

  while queue:
    vertex = queue.popleft()   # Dequeue a vertex from the queue
    print(vertex)   # Process the vertex (in this case, print it)
    visited.add(vertex)   # Mark the vertex as visited

    # Enqueue all adjacent vertices that haven't been visited
    for neighbor in graph[vertex]:
      if neighbor not in visited:
        queue.append(neighbor)

my_graph = {
  "A": ["B", "C"],
  "B": ["D", "E"],
  "C": ["F"],
  "D": [],
  "E": ["F"],
  "F": []
}

bfs((my_graph), "A")