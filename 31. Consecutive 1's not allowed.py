#https://www.geeksforgeeks.org/problems/consecutive-1s-not-allowed1912/1

class Solution:

	def countStrings(self,n):
    	# code here
    	#fibonachi
    	dp=[2,3]
    	for i in range(2,n):
    	    dp.append(dp[i-1]+dp[i-2])
    	return dp[n-1]
    	
