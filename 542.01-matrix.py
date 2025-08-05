# @leet start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque([])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = -1

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                # check a direction, this is the nextrow/nextcol to check
                nr = row + dr
                nc = col + dc
                # check if this next node is visited or out of bounds
                # if so skip this loop iteration
                if nr < 0 or nr == len(mat) or nc < 0 or nc == len(mat[0]) or mat[nr][nc] != -1:
                    continue
                # not visited, we add 1 to the row/col we are at and set it to this next node
                mat[nr][nc] = mat[row][col] + 1
                # add this node back in to the queue to check its neighbors
                queue.append((nr, nc))
            # loop ends once we've visted every node and set their distance
            # doesn't a higher distance than possible because we do the queue in order:
            # 0s added to queue first, then everything 1 away from the 0s that is valid
            # effectively a Breadth First Search (BFS) method
        return mat

def printMatrix(mat):
    print('mat: ')
    for row in mat:
        print(row)
# @leet end
