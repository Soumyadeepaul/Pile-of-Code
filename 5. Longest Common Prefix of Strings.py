#https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1

class Solution:
    def longestCommonPrefix(self, arr):
        prefix=arr[0] #let the 1st element be longest prefix
        for i in arr[1:]:
            j=0
            if len(i)<len(prefix):
                prefix,i=i,prefix
            while j<len(prefix):
                if prefix[j]==i[j]:
                    pass
                else:
                    break
                j+=1
            prefix=prefix[:j]
        return prefix
