class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        result = 0
        
        if root is None:
            return result
        
        stack = [root]
        
        while stack:
            curr = stack.pop()
            
            if curr.val >= L and curr.val <= R:
                result += curr.val
            
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return result
