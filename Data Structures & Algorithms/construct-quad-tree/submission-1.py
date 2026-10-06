"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        root = Node(val = True, isLeaf = False)
        if len(grid) == 0:
            return Node(False, True)

        def helper(grid):
            if len(grid) == 0:
                return Node(False, True)
                
            n = len(grid) // 2


            grid_top_left = [x[0:n] for x in grid[0:n]]
            grid_top_right = [x[n:] for x in grid[0:n]]
            grid_bottom_left = [x[0:n] for x in grid[n:]]
            grid_bottom_right = [x[n:] for x in grid[n:]]

            elements = set()

            for row in grid:
                for col in row:
                    elements.add(col)

            

            if len(elements) > 1:

                new_root = Node(isLeaf = False, val = 1)
                
                new_root.topLeft = helper(grid_top_left)
                new_root.topRight = helper(grid_top_right)
                new_root.bottomLeft = helper(grid_bottom_left)
                new_root.bottomRight = helper(grid_bottom_right)

                return new_root
            elif 1 in elements:
                return Node(val = 1, isLeaf = True)
            elif 0 in elements:
                return Node(val = 0, isLeaf = True)

            
        root = helper(grid)
        return root



            