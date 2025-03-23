#https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        #Using nested loop
        # for i in range(len(arr)):
        #     summ=0
        #     for j in range(i,len(arr)):
        #         summ+=arr[j]
        #         if summ==target:
        #             return [i+1,j+1]
        #         elif summ>target:
        #             break
        # return [-1]
        
        
        
        ###################################
        #prefix sum
        #used unorderd list for O(1) search time complexity
        prefixSum={}
        summ=0
        for j in range(len(arr)):
            #not using extra loop for prefixSum calculation prehand
            summ+=arr[j]
            #is same element repeats in arr
            if summ not in prefixSum:
                prefixSum[summ]=j
            ##############
            #finding the window size using prefixsum
            #summ-target is used because summ is the key... if we do prefixSum[summ] it will return value/position 
            val=summ-target
            #if val is 0... means 1st index
            #indexing starts at 1
            if not val:
                return [1,j+1]
            if val in prefixSum:
                return [prefixSum[val]+2,j+1]
        return [-1]
