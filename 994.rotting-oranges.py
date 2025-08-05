# @leet start
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cycles = 0
        rot_queue = deque([])
        # make a queue to specify the order that rotting tales place
        # must be done due to the possibility of multiple rotten oranges in a
        # given 'island' of oranges
        
        # loop through grid to fins all rotten orange locations and queue them up
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rot_queue.append((row, col))

        while rot_queue:
            # need a way to distinguish between each new cycle of rotten
            new_cycle_queue = deque([])
            while rot_queue:
                row, col = rot_queue.popleft()
                # check adjacent oranges to rot
                for d in directions:
                    dx, dy = d
                    dr = row + dx
                    dc = col + dy
                    if 0 <= dr < len(grid) and 0 <= dc < len(grid[row]):
                        if grid[dr][dc] == 1:
                            grid[dr][dc] = 2
                            new_cycle_queue.append((dr, dc))
            rot_queue = new_cycle_queue
            if rot_queue:
                cycles += 1

        # check if any fresh oranges (1) remain in grid, otherwise return cycles
        for row in grid:
            return -1
        return cycles
# @leet end
