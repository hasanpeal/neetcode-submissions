class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        
        count = 0
        
        adj = defaultdict(list)
        visited = set()
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count