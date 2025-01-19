def is_safe(maze, x, y, solution):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1 and solution[x][y] == 0

def solve_maze(maze):
    n, m = len(maze), len(maze[0])
    solution = [[0 for _ in range(m)] for _ in range(n)]

    def solve(x, y):
        if x == n - 1 and y == m - 1:  # Reached destination
            solution[x][y] = 1
            return True
        if is_safe(maze, x, y, solution):
            solution[x][y] = 1
            if solve(x + 1, y) or solve(x, y + 1):
                return True
            solution[x][y] = 0  # Backtrack
        return False

    if solve(0, 0):
        return solution
    else:
        return "No solution exists."

# Example Maze
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solution = solve_maze(maze)
print("Solution Path:")
if isinstance(solution, str):
    print(solution)
else:
    for row in solution:
        print(row)
