from collections import deque

def get_graph_input():
    graph = {}
    print("Enter the graph as an adjacency list. Type '-1' when finished \n")

    while True:
        node = input("Enter node: ").strip()
        if node.lower() == '-1':
            break

        adj_nodes = input(f"Enter neighbors for {node} (use comma): ").strip().split(',')
        adj_nodes = [n.strip() for n in adj_nodes]

        graph[node] = adj_nodes
    return graph


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        # print(vertex)
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)


def startCalculation():

    graph = get_graph_input()
    print(graph)

    start_node = input("Enter the starting node for BFS: ").strip()

    print("BFS Traversal Order:")
    bfs(graph, start_node)

startCalculation()