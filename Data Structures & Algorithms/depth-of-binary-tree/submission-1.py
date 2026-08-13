class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def solve(node):
            if node is None:
                return 0

            left_side = solve(node.left)
            right_side = solve(node.right)

            return 1 + max(left_side, right_side)

        return solve(root)