
# calculate dfs
def calculate_dfs(graphs, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for neighbor in graphs[start]:
        if neighbor not in visited:
            calculate_dfs(graphs, neighbor, visited)


# graph input
graph = {}
vertices_input = input("Enter vertices (space-separated): ").strip()
vertices = vertices_input.split()

# set empty array for every vertex
for v in vertices:
    graph[v] = []

print("\nAdd edges. Type '-1' to stop")

# get input
while True:
    select = input("Select vertex to add edges to: ").strip()
    if select.lower() == '-1':
        break
    if select not in graph:
        print("Vertex not found. Try again.")
        continue

    points = input(f"Enter neighbors of {select} (space-separated): ").strip().split()
    graph[select].extend(points)

# display the graph
print("\nGraph:", graph)

# start
start_point = input("\nEnter starting point for DFS: ").strip()

# calculate dfs
calculate_dfs(graph, start_point)

