class Solution:
    def fill(self, n, m, mat):
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != 'O':
                return
            
            mat[i][j] = 'S'  # Mark as safe
            
            # Check in all 4 directions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # Step 1: Mark 'O's connected to border as safe
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
        
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)
        
        # Step 2: Replace remaining 'O's with 'X's and 'S's with 'O's
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O':
                    mat[i][j] = 'X'
                elif mat[i][j] == 'S':
                    mat[i][j] = 'O'
        
        return mat

# Example usage (not needed for submission)
# sol = Solution()
# mat = [['X', 'X', 'X', 'X'], 
#        ['X', 'O', 'X', 'X'], 
#        ['X', 'O', 'O', 'X'], 
#        ['X', 'O', 'X', 'X'], 
#        ['X', 'X', 'O', 'O']]
# n, m = 5, 4
# result = sol.fill(n, m, mat)
# for row in result:
#     print(row)
