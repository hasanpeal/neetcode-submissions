class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []  # Initialize 'res' to store all valid combinations and 'sol' for the current combination
        nums = candidates   # Use 'nums' as a shorthand for the input 'candidates' list
        n = len(nums)       # Get the number of candidates

        def backtrack(i, cur_sum):
            # Base case: If the current sum equals the target
            if cur_sum == target:
                res.append(sol[:]) # Add a *copy* of the current combination 'sol' to the results
                return

            # Pruning conditions: If current sum exceeds target or all candidates are processed
            if cur_sum > target or i == n:
                return

            # Decision 1: Exclude the current candidate nums[i]
            # Move to the next candidate (i+1) without adding nums[i] to 'sol'
            backtrack(i+1, cur_sum)

            # Decision 2: Include the current candidate nums[i]
            sol.append(nums[i])  # Add nums[i] to the current combination
            # Recursively call backtrack with the same candidate 'i' (allowing reuse)
            # and the updated sum
            backtrack(i, cur_sum + nums[i])
            sol.pop()  # Backtrack: remove nums[i] to explore other possibilities

        backtrack(0, 0)  # Start the backtracking process from the first candidate (index 0) with sum 0
        return res       # Return the list of all found combinations
