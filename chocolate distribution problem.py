class Solution:

    def findMinDiff(self, A,N,M):
        # code here
        A.sort()
        minimum = float("inf")
        i = 0
        
        while i < N-M+1:
            minimum = min(abs(A[i+M-1] - A[i]), minimum)
            
            i += 1
            
        return minimum

