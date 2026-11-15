class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        if len(edges) > (n - 1):
            return False
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node, prevNode):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == prevNode:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n