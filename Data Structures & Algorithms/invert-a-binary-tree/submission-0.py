class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Base case
        if root is None:
            return None

        # Swap the left and right child
        root.left, root.right = root.right, root.left

        # Invert the left subtree
        self.invertTree(root.left)

        # Invert the right subtree
        self.invertTree(root.right)

        return root