def numIslands(self, grid: List[List[str]]) -> int:
    island_graph = {}
    # Construct the graph of possible islands.
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != "1":
                continue
            neighbors = []
            if row-1 >= 0 and grid[row-1][col] == "1":
                neighbors.append((row-1, col))
            if row+1 < len(grid) and grid[row+1][col] == "1":
                neighbors.append((row+1, col))
            if col-1 >= 0 and grid[row][col-1] == "1":
                neighbors.append((row, col-1))
            if col+1 < len(grid[row]) and grid[row][col+1] == "1":
                neighbors.append((row, col+1))
            island_graph[(row, col)] = neighbors
    
    # Navigate the possible islands.
    def _dfs(curr, graph, grid):
        if grid[curr[0]][curr[1]] == "2":
            return 0
        grid[curr[0]][curr[1]] = "2"
        # Visit all neighbors
        for neighbor in graph[curr]:
            _dfs(neighbor, graph, grid)
        return 1
    
    count = 0
    for island in island_graph:
        count += _dfs(island, island_graph, grid)

    return count 






