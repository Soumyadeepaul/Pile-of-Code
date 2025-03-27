#https://www.geeksforgeeks.org/problems/sum-tree/1

class Solution:
    def is_sum_tree(self, node):
        # code here
        #postorder Traversal
        
        def postorder(node,summ):
            #if criteria fails
            if summ==-1:
                return -1
            if node:
                #leaf node
                if node.left==None and node.right==None:
                    return node.data
                #left side summation
                val1=0
                if node.left:
                    val1=postorder(node.left,summ)
                #right side summation
                val2=0
                if node.right:
                    val2=postorder(node.right,summ)
                #check for present subtree
                summ=val1+val2
                #if present subtree fullfill criteria
                if node.data==summ:
                    #return the subtree summ + the root of the subtree
                    return summ+node.data
                else:
                    #if criteria fails
                    return -1
        summ=postorder(node,0)
        if summ==-1:
            return False
        return True
