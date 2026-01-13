# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if p.val > q.val:
            lower = q.val
            higher = p.val
        else:
            higher = q.val
            lower = p.val
        
        return self.check(root, lower, higher)
    
    def check(self, root, lower, higher):
        if root and (root.val == lower or root.val == higher):
            return root
        
        if root and root.left and root.right:
            if root.val > lower and root.val < higher:
                return root
            elif root.val < lower:
                return self.check(root.right, lower, higher)
            elif root.val > higher:
                return self.check(root.left, lower, higher)