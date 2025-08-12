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


def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # Make graph
    graph = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != 1:
                continue
            neighbors = []
            # check up
            if r-1 >= 0 and grid[r-1][c] == 1:
                neighbors.append((r-1, c))
            # check down
            if r+1 < len(grid) and grid[r+1][c] == 1:
                neighbors.append((r+1, c))
            # check left
            if c-1 >= 0 and grid[r][c-1] == 1:
                neighbors.append((r, c-1))
            # check right
            if c+1 < len(grid[r]) and grid[r][c+1] == 1:
                neighbors.append((r, c+1))
            graph[(r, c)] = neighbors
    
    # dfs to traverse graph
    def _dfs(current, graph, grid):
        if grid[current[0]][current[1]] == 2:
            return 0
        # Visit this. 
        grid[current[0]][current[1]] = 2
        # Check all neighbors
        count = 0
        for neighbor in graph[current]:
            count += _dfs(neighbor, graph, grid)
        return 1 + count
    
    # Run DFS on all the island candidates.
    maximum_area = 0
    for island in graph:
        area = _dfs(island, graph, grid)
        if area > maximum_area:
            maximum_area = area

    return maximum_area


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    vertex_dict = {} # Make a mapping of old : new
    
    def _dfs(visited, current, vertex_dict):
        if current.val in visited:
            return
        visited.add(current.val)
        new_node = Node(current.val)
        vertex_dict[current] = new_node
        # print(f"Added {current.val} node")
        # Visit all other nodes and get them.
        for neighbor in current.neighbors:
            _dfs(visited, neighbor, vertex_dict)
        return
    
    def _constructNewGraph(visited, current, vertex_dict):
        if current.val in visited:
            return
        visited.add(current.val)
        for neighbor in current.neighbors:
            vertex_dict[current].neighbors.append(vertex_dict[neighbor])
            _constructNewGraph(visited, neighbor, vertex_dict)

    if node is None:
        return None
    
    visited = set()
    _dfs(visited, node, vertex_dict)
    visited = set()
    _constructNewGraph(visited, node, vertex_dict)
    return vertex_dict[node]


def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    from collections import deque
    queue = deque()
    inf = (2 ** 31) - 1
    visited = set()
    # Find and place the treasure cells into the deque
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                queue.appendleft((r, c))
    
    level = 0
    while queue:
        # Pop all the cells.
        cells = []
        while queue:
            cells.append(queue.pop())
        for cell in cells:
            r, c = cell[0], cell[1]
            # Update the entry
            grid[r][c] = level
            # Enqueue the neighbors if possible.
            if r - 1 >= 0 and grid[r-1][c] == inf and (r-1, c) not in visited:
                queue.appendleft((r-1, c))
                visited.add((r-1, c))            
            if r + 1 < len(grid) and grid[r+1][c] == inf and (r+1, c) not in visited:
                queue.appendleft((r+1, c))
                visited.add((r+1, c))            
            if c - 1 >= 0 and grid[r][c-1] == inf and (r, c-1) not in visited:
                queue.appendleft((r, c-1))
                visited.add((r, c-1))            
            if c + 1 < len(grid[0]) and grid[r][c+1] == inf and (r, c+1) not in visited:
                queue.appendleft((r, c+1))
                visited.add((r, c+1))            
        level += 1

                
def orangesRotting(self, grid: List[List[int]]) -> int:
    '''
        Use multi-source BFS
    '''
    from collections import deque
    queue = deque()
    visited = set()
    # Find all rotten fruit.
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                queue.appendleft((r, c))
    
    time = 0
    while queue:
        print(f"Queue at time {time} {queue}")
        # Pop all
        fruits = []
        while queue:
            fruit = queue.pop()
            visited.add(fruit)
            fruits.append(fruit)
        
        # Enqueue all neighbors and set to rotten.
        for fruit in fruits:
            grid[fruit[0]][fruit[1]] = 2
            r, c = fruit
            # Up
            if r - 1 >= 0 and grid[r-1][c] != 0 and (r-1, c) not in visited:
                visited.add((r-1, c))
                queue.appendleft((r-1, c))
            # Down
            if r + 1 < len(grid) and grid[r+1][c] != 0 and (r+1, c) not in visited:
                visited.add((r+1, c))
                queue.appendleft((r+1, c))
            # Left
            if c - 1 >= 0 and grid[r][c-1] != 0 and (r, c-1) not in visited:
                visited.add((r, c-1))
                queue.appendleft((r, c-1))
            # Right
            if c + 1 < len(grid[0]) and grid[r][c+1] != 0 and (r, c+1) not in visited:
                visited.add((r, c+1))
                queue.appendleft((r, c+1))
        
        time += 1


    # Check if any fresh fruit left.
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                return -1

    return 0 if time == 0 else time-1

        








