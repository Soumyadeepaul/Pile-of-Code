#https://www.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1

class Solution:
    def minDepth(self, root):
        #Code here
        if root:
            #if leaf node
            if root.left==None and root.right==None:
                return 1
            #if right child exist... go right and 1+ (for internal node)
            if root.left==None:
                return 1+self.minDepth(root.right)
            #if left child exist... go left and 1+ (for internal node)
            if root.right==None:
                return 1+self.minDepth(root.left)
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))  # minimum depth from both side  1+ (for internal node)
