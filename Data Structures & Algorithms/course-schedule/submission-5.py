class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            adjacencyList[c].append(p)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adjacencyList[course] == []:
                return True
            visited.add(course)
            for pre in adjacencyList[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            adjacencyList[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
