# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # make a queue to keep a list of neighbors to make,
        # make the neighbors nodes and store them in a list to check if a neighbor needs to be made
        # once no new neighbors need to be made all nodes have been made.
        # reverse through the list and properly populate their neighbor lists
        # print('start')
        queue = deque([])
        nodes = []
        nodes_visited = []
        # print('checking default node provided')
        # print(node)
        if node:
            # node.val should be 1
            # print('node exists')
            new_root = Node(1, [])
            c = []
            for m in node.neighbors:
                c.append(m.val)
            nodes.append([new_root, c])
            nodes_visited.append(1)
        else:
            # print('no node found')
            return None
        # print('past start')
        for n in node.neighbors:
            queue.append(n)
        # print(queue)
        while queue:
            n = queue.popleft()
            if n.val not in nodes_visited:
                nodes_visited.append(n.val)
                new_node = Node(n.val, [])
                c = []
                for m in n.neighbors:
                    c.append(m.val)
                    if m.val not in nodes_visited and m.val not in queue:
                        queue.append(m)
                nodes.append([new_node, c])
        for i in nodes:
            for j in nodes:
                # print(j[0].val)
                # print(i[1])
                if j[0].val in i[1]:
                    # print('adding neighbor')
                    i[0].neighbors.append(j[0])
                    # print(i[0].neighbors)


        return new_root
# @leet end
