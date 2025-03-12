#https://www.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1

class Solution:
    def getCount(self, root, l, h):
        # Your code here
        if root:
            le=re=0
            if root.data>l:   #as it follows bst
                le=self.getCount(root.left,l,h)   
            if root.data<h:
                re=self.getCount(root.right,l,h)
            if root.data>=l and root.data<=r:    #only count when data in range
                return 1+le+re
            else:
                return le+re   #if intermediate node is not in range, therefore pass the value as it is
        return 0
