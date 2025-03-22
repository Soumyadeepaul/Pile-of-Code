#https://www.geeksforgeeks.org/problems/majority-element-1587115620/1

class Solution:
    def majorityElement(self, arr):
        #Your code here
        dic={}
        majority=0
        majorityVal=0
        for i in arr:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
            if dic[i]>majorityVal:
                majorityVal=dic[i]
                majority=i
        if majorityVal<=len(arr)//2:
            return -1
        return majority
