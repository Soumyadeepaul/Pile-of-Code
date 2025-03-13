#https://www.geeksforgeeks.org/problems/check-for-bst/1

class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def iBST(root,result):
            if root.left:
                r=iBST(root.left,result)
                if r==0:
                    return 0
            if result[-1]<root.data:
                result.append(root.data)
            else:
                return 0
            if root.right:
                r=iBST(root.right,result)
                if r==0:
                    return 0
            return 1
        current=[-9999999]
        r=iBST(root,current)
        return r
