#https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        largestSum=-9999999999999
        summ=0
        for i in range(len(arr)):
            summ+=arr[i]
            if largestSum<summ:
                largestSum=summ
            if summ<0:
                summ=0
        return largestSum
