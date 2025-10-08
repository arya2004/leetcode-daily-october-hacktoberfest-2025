class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]
      
        n = len(grid)

        parent = list(range(n * n))

        elevation_to_position = [0] * (n * n)
        for row_idx, row in enumerate(grid):
            for col_idx, elevation in enumerate(row):
                elevation_to_position[elevation] = row_idx * n + col_idx

        for time in range(n * n):
            current_cell_idx = elevation_to_position[time]
            current_row = current_cell_idx // n
            current_col = current_cell_idx % n
          
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            for delta_row, delta_col in directions:
                neighbor_row = current_row + delta_row
                neighbor_col = current_col + delta_col
              
                if (0 <= neighbor_row < n and 
                    0 <= neighbor_col < n and 
                    grid[neighbor_row][neighbor_col] <= time):
                  
                    neighbor_idx = neighbor_row * n + neighbor_col
                    parent[find(neighbor_idx)] = find(current_cell_idx)
              
                start_idx = 0
                end_idx = n * n - 1
                if find(start_idx) == find(end_idx):
                    return time
      
        return -1
