class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        tree = defaultdict(list)

        for edge in edges:
            start, end = edge[0], edge[1]

            tree[start].append(end)
            tree[end].append(start)

        seen = set()
        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)
            for connected_node in tree[node]:
                if connected_node == prev:
                    continue
                if not dfs(connected_node, node):
                    return False

            return True

        return dfs(0, -1) and len(seen) == n
