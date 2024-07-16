class Solution:
    def findMinDiff(self, A, N, M):
        # If there are no chocolates or number of students is 0, 
        # no distribution is possible
        if N == 0 or M == 0:
            return 0
        
        # If there are more students than packets, 
        # distribution is not possible
        if M > N:
            return -1
        
        # Sort the array of chocolates
        A.sort()
        
        min_diff = float('inf')
        
        # Find the subarray of size M with the minimum difference 
        # between the first and the last element
        for i in range(N - M + 1):
            diff = A[i + M - 1] - A[i]
            min_diff = min(min_diff, diff)
        
        return min_diff
