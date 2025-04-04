#https://www.geeksforgeeks.org/problems/coin-change2448/1

class Solution:
    def count(self, coins, sum):
        # code here 
        dp=[[0 for _ in range(sum+1)]for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            for j in range(sum+1):
                if j==0:
                    dp[i][j]=1
                if i==0 and j>0:
                    dp[i][j]=0
                elif i>0 and j>0:
                    if coins[i-1]>j:
                        dp[i][j]=dp[i-1][j]
                    else:
                        #here summation of previous row same column with same row j-coin column
                        dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
        return dp[len(coins)][sum]
