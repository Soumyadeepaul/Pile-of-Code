#https://www.geeksforgeeks.org/problems/level-order-traversal/1

class Solution:
    def levelOrder(self, root):
        # Your code here
        queue=[root]
        result=[[root.data]]
        while queue:
            val=queue.pop(0)
            new=[]
            if val.left:
                queue.append(val.left)
                new.append(val.left.data)
            if val.right:
                queue.append(val.right)
                new.append(val.right.data)
            if new:
                result.append(new)
        return result
