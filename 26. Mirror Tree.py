#https://www.geeksforgeeks.org/problems/mirror-tree/1


class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        if root:
            if root.left and root.right:
                right=root.left
                root.left=root.right
                root.right=right
                self.mirror(root.left)
                self.mirror(root.right)
            elif root.right:
                root.left=root.right
                root.right=None
                self.mirror(root.left)
            elif root.left:
                root.right=root.left
                root.left=None
                self.mirror(root.right)
        return
