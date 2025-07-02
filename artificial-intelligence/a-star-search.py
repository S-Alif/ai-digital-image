import heapq

# Define the grid and possible moves (4 directions: up, down, left, right)
GRID = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

# Directions for movement (up, down, left, right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search algorithm
def a_star_search(start, goal):
    # Open set is a priority queue (min-heap) for nodes to explore
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))  # (F, G, position)

    # To track the path
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        # Pop the node with the lowest F value
        _, g, current = heapq.heappop(open_set)
        
        # If we reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        # Explore neighbors
        for move in MOVES:
            neighbor = (current[0] + move[0], current[1] + move[1])

            # Check if the neighbor is within bounds and walkable
            if 0 <= neighbor[0] < len(GRID) and 0 <= neighbor[1] < len(GRID[0]) and GRID[neighbor[0]][neighbor[1]] == 1:
                tentative_g_score = g + 1  # Assume cost to move to neighbor is 1

                # If we found a better path to the neighbor, or it hasn't been visited
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))

    return None  # No path found

# User input for start and goal positions
def get_user_input():
    print("Enter the start position (row, column): ")
    start_row, start_col = map(int, input().split())
    print("Enter the goal position (row, column): ")
    goal_row, goal_col = map(int, input().split())
    
    start = (start_row, start_col)
    goal = (goal_row, goal_col)

    # Ensure the start and goal are walkable
    if GRID[start_row][start_col] == 0 or GRID[goal_row][goal_col] == 0:
        print("Start or goal is not walkable!")
        return None, None
    
    return start, goal

# Run the program
if __name__ == "__main__":
    start, goal = get_user_input()
    
    if start and goal:
        path = a_star_search(start, goal)
        if path:
            print("Path found:", path)
        else:
            print("No path found!")
