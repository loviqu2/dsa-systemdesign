
#Binary Search Tree, BST only allows left side of the child tree to be smaller than the right side


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bst_search(node, target):
    if node is None:  # if node is None then false
        return False
    if node.value == target: #if node is target return true
        return True
    elif target < node.value: #search if the target is bigger or smaller than the node, then return the func, until node value is the target
        return bst_search(node.left, target)
    else:
        return bst_search(node.right, target)
    


node = TreeNode(10)
node.left = TreeNode(5)
node.right = TreeNode(15)
node.left.left = TreeNode(3)
node.left.right = TreeNode(7)
node.right.right = TreeNode(20)

print(bst_search(node, 3))    # expect True
print(bst_search(node, 20))   # expect True
print(bst_search(node, 100))  # expect False