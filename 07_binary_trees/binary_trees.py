#DFS
#Preorder traversal

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node is None: #if none then stop.
        return
    print(node.value) #print the current value, should start at the top 
    preorder(node.left) # go down left, if there is nothing else left ( it pauses here until whole subleft tree finished)
    preorder(node.right) 

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

preorder(root)