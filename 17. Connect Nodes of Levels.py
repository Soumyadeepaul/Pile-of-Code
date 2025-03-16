#https://www.geeksforgeeks.org/problems/connect-nodes-at-same-level/1


import sys
sys.setrecursionlimit(50000)
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        
        #BFS
        queue=[root]
        newLevelQueue=[]
        while queue:
            val=queue.pop(0)
            if val.left!=None and val.right!=None:
                newLevelQueue.extend([val.left,val.right])
            elif val.left:
                newLevelQueue.append(val.left)
            elif val.right:
                newLevelQueue.append(val.right)
            if len(queue)==0:
                for i in range(len(newLevelQueue)-1):
                    newLevelQueue[i].nextRight=newLevelQueue[i+1]
                queue=newLevelQueue
                newLevelQueue=[]
        return root
