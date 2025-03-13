#https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

class Solution:
    def subarraySum(self, arr, target):
        # code here
        for i in range(len(arr)):
            summ=0
            for j in range(i,len(arr)):
                summ+=arr[j]
                if summ==target:
                    return [i+1,j+1]
                elif summ>target:
                    break
        return [-1]
