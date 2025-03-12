#https://www.geeksforgeeks.org/problems/find-first-and-last-occurrence-of-x0849/1

class Solution:
    def indexes(self, v, x):
        # Your code goes here
        left=0
        foundLeft=-1
        foundRight=-1
        while left<len(v):
            if v[left]==x:
                foundLeft=left
                break
            else:
                left+=1
        v.append('-')
        while left<len(v)-1:
            if v[left]==v[left+1]:
                left+=1
            else:
                foundRight=left
                break
        if v[left]==x:
            foundRight=left
        return [foundLeft,foundRight]
