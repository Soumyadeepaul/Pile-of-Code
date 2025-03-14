#https://www.geeksforgeeks.org/problems/implement-strstr/1

class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        for i in range(len(txt)):
            if txt[i]==pat[0]:
                match=1
                for j in range(1,len(pat)):
                    if j+i<len(txt):
                        if txt[i+j]!=pat[j]:
                            match=0
                            break
                if match==1:
                    return i
        return -1
