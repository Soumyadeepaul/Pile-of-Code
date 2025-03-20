#https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

class Solution:
    def getPairs(self, arr):
        # code here
        arr=sorted(arr)
        result=[]
        j=len(arr)-1
        i=0
        while i<j:
            if i!=0 and arr[i]==arr[i-1]:
                i+=1
                pass
            else:
                target=-arr[i]
                if arr[j]>target:
                    j-=1
                elif arr[j]==target:
                    result.append([arr[i],arr[j]])
                    i+=1
                    j-=1
                else:
                    i+=1
            
        return result
