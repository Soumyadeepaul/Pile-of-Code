#https://www.geeksforgeeks.org/problems/reverse-each-word-in-a-given-string1001/1

class Solution:
    # Function to reverse words in a given string
    def reverseWords(self, s: str) -> str:
        #code here
        s=list(s)
        while s[0]==' ':
            s=s[1:]
        while s[-1]==' ':
            s=s[:-1]
        s=s+[' ']
        i=0
        while i<len(s):
            if s[i]==' ': #checking of extra space
                s.pop(i)
            else:
                start=i
                for j in range(i,len(s)):
                    if s[j]==' ':
                        break
                nextPos=j
                j-=1
                while start<j:
                    s[start],s[j]=s[j],s[start]
                    start+=1
                    j-=1
                i=nextPos+1 #space is getting counted here
        return ''.join(s[:-1])
                
