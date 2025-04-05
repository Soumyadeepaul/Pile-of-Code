#https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

class Solution:
    def countFreq(self, arr, target):
        #code here
        count=0
        for i in arr:
            if i!=target and count!=0:
                break
            elif i==target:
                count+=1
        return count
