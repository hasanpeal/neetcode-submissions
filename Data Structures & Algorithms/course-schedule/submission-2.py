class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create a dictionary to store prerequisites for each course
        # Key: course, Value: list of prerequisites for that course
        preq = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preq[c].append(p)
        
        # Step 2: Create a set to track visited courses during DFS
        # This set is used to detect cycles in the prerequisite dependency graph
        visited = set()

        # Step 3: Define a recursive function to detect cycles in the prerequisite graph
        def dfsCycleDetect(c):
            # If the current course is already in the visited set, a cycle is detected
            if c in visited:
                return False
            
            # If the current course has no prerequisites, it can be completed
            if preq[c] == []:
                return True
            
            # Add the current course to the visited set (marking it as being processed)
            visited.add(c)
            
            # Recursively check all prerequisites for the current course
            for pre in preq[c]:
                # If any prerequisite cannot be completed (cycle detected), return False
                if not dfsCycleDetect(pre):
                    return False
            
            # Remove the course from the visited set after processing its prerequisites
            # This allows other paths in the graph to explore this course if needed
            visited.remove(c)
            
            # Mark the course as completed by clearing its prerequisites (optimization step)
            preq[c] = []
            
            # If all prerequisites are successfully completed, return True
            return True

        # Step 4: Iterate through all courses to ensure they can all be completed
        for p in range(numCourses):
            # If any course cannot be completed due to a cycle, return False
            if not dfsCycleDetect(p):
                return False
        
        # If all courses can be completed, return True
        return True

