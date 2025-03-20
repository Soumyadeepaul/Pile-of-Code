#https://www.geeksforgeeks.org/problems/addition-of-submatrix5835/1

class Solution:

	def subMatrixSum(self,arr, n, m, x1, y1, x2, y2):
		# code here
		summ=0
		for i in range(x1-1,x2):
		    for j in range(y1-1,y2):
		        summ+=arr[i][j]
		return summ
