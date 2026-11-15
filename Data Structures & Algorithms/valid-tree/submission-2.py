class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        if len(edges) > (n - 1):
            return False
        
        adj = defaultdict(list)
        visited = set()
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(curr, prev):
            if curr in visited:
                return False
            visited.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n


        