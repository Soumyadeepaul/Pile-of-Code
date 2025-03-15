#https://www.geeksforgeeks.org/problems/finding-the-numbers0215/1

class Solution:
	def singleNumber(self, arr):
		# Code here
		if len(arr)==1:
		    return arr
		arr=sorted(arr)
		ans=[]
		if arr[0]!=arr[1]:
		    ans.append(arr[0])
		for i in range(1,len(arr)-1):
		    if arr[i-1]!=arr[i] and arr[i]!= arr[i+1]:
		        ans.append(arr[i])
		if arr[-1]!=arr[-2]:
		    ans.append(arr[-1])
		return ans
