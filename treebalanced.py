class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def height(root):

    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def is_balanced(root):

    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    
    return False


balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(3)
balanced_root.left.left = TreeNode(4)
balanced_root.left.right = TreeNode(5)
unbalanced_root = TreeNode(1)
unbalanced_root.left = TreeNode(2)
unbalanced_root.right = TreeNode(3)
unbalanced_root.left.left = TreeNode(4)
unbalanced_root.left.left.left = TreeNode(5)

print("Is the balanced binary tree balanced?", is_balanced(balanced_root))
print("Is the unbalanced binary tree balanced?", is_balanced(unbalanced_root))