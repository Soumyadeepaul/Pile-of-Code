#https://www.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1

#ANAGRAM means when one word can be formed from rearranging another word

class Solution:
    def areKAnagrams(self, s1, s2, k):
        # code here
        if len(s1)!=len(s2):
            return False
        wordsFreq={}
        #Frequency Technique
        for i in range(len(s1)):
            if s1[i] not in wordsFreq.keys():
                wordsFreq[s1[i]]=1
            else:
                wordsFreq[s1[i]]+=1
        
        for i in range(len(s2)):
            #if not in wordsFreq... means we have to change that alphabet.....therefore k-=1
            if s2[i] not in wordsFreq.keys():
                if k==0:
                    return False
                k-=1
            else:
                #if found in wordsfreq and value not 0... no need to reduce k
                #reduce k only when value is 0..... and break when need to change but k==0
                if wordsFreq[s2[i]]!=0:
                    wordsFreq[s2[i]]-=1
                else:
                    if k==0:
                        return False
                    k-=1
        return True
