#https://www.geeksforgeeks.org/problems/root-to-leaf-path-sum/1

#User function Template for python3
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        # code here
        
        
        #preorder
        if root:
            #backtracking
            #######
            target-=root.data
            #######
            if target==0:
                #should not be internal Node
                if root.left or root.right:
                    return False
                return True
            val1=self.hasPathSum(root.left,target)
            val2=self.hasPathSum(root.right,target)
            #if got value true... send back true for exit
            if val1==True or val2==True:
                return True
            #backtracking... seting target to old value
            ######
            target+=root.data
            ######
        return False
