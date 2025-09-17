"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# https://leetcode.com/problems/clone-graph/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class Solution:
    def traverse(self, node, visited):
        # 1. A typical DFS traversal - traverse through the neighbours of a node
        if node.val in visited:
            return visited[node.val]

        neighbor_nodes = []
        new_node = Node(node.val, neighbor_nodes)
        # 2. A catch however, is that we need to save it into the visited array BEFORE we visit its neighbors
        #   - This is even though the Node's final result depends on the traversal results (pointers to its neighbour nodes)
        #   - neighbor_nodes[] is a pointer and can be modified even after being instantinated into Node
        visited[node.val] = new_node
        for neighbor in node.neighbors:
            neighbor_nodes.append(self.traverse(neighbor, visited))

        return new_node

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        visited = {}

        return self.traverse(node, visited)
