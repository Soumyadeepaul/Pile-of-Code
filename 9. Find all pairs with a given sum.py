#https://www.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/1

class Solution:
    def allPairs(self, target, arr1, arr2):
        # Your code goes here 
        result=[]
        arr1=sorted(arr1)
        arr2=sorted(arr2)
        pos=len(arr2)-1
        for i in range(len(arr1)):
            # if the value is same as previous in arr1
            if i!=0 and arr1[i]==arr1[i-1]:
                result.extend(added)
            else:
                val=target-arr1[i]
                added=[]
                #start loop from where it ended before
                for j in range(pos,-1,-1):
                    if arr2[j]==val:
                        added.append([arr1[i],arr2[j]])
                    elif arr2[j]<val:
                        pos=j
                        break
                if len(added)!=0:
                    result.extend(added)
        return result
