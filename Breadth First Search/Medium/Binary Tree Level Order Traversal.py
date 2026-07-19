# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class QueueNode:
    def __init__(self, depth, node):
        self.depth = depth
        self.node = node

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Breath First Search
        # - While maintaing which "Depth" we are at (DFS)
        start = 0
        queue = [QueueNode(0, root)]
        result = []
        while start != len(queue):
            #       3
            #     9   20
            #   11 12 13 14
            #  --> Go left first
            queue_node = queue[start]
            start += 1
            if queue_node.node is None:
                continue
            
            # Need level-by-level array
            # -> Mimic a DFS concept of "depth" by giving each node a DEPTH
            if queue_node.depth >= len(result): # First node in depth, append a new array
                result.append([queue_node.node.val]) 
            else:
                result[queue_node.depth].append(queue_node.node.val) # Existing nodes in depth, append to existing array
            
            queue.append(QueueNode(queue_node.depth+1, queue_node.node.left))
            queue.append(QueueNode(queue_node.depth+1, queue_node.node.right))
        
        return result
