#https://www.geeksforgeeks.org/problems/anagram-1587115620/1


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        dic={}
        if len(s1)!=len(s2):
            return False
        i=0
        while i<len(s1):
            if s1[i] not in dic:
                dic[s1[i]]=1
            else:
                dic[s1[i]]+=1
            i+=1
        j=0
        
        while j<len(s2):
            if s2[j] not in dic.keys():
                return False
            else:
                dic[s2[j]]-=1
                if dic[s2[j]]<0:
                    return False
            j+=1
        for i in dic.values():
            if i!=0:
                return False
        return True
