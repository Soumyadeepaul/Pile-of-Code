#https://www.geeksforgeeks.org/problems/generate-binary-string3642/1


class Solution:
    def generate_binary_string(self,s):
        count=0
        for i in s:
            if i=='?':
                count+=1
        if count==0:
            return [s]
        queue=[s]
        new_i=0
        ans=[]
        count_Match=0
        while queue:
            string=queue.pop(0)
            i=new_i
            while i<len(string):
                if string[i]=='?':
                    if i==0:
                        count_Match+=1
                    elif i==new_i:
                        pass
                    else:
                        count_Match+=1
                    if i<len(s):
                        new_str1=string[:i]+'0'+string[i+1:]
                        new_str2=string[:i]+'1'+string[i+1:]
                    else:
                        new_str1=string[:i]+'0'
                        new_str2=string[:i]+'1'
                    if count==count_Match:
                        ans.extend([new_str1,new_str2])
                    else:
                        queue.extend([new_str1,new_str2])
                    new_i=i
                    break
                        
                i+=1
        return ans
