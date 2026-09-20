
#Breadth first search, uses a queue method, First In First Out (FIFO), processed by queue order, not parent or child relationship

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    queue = [root]
    while queue: #while the queue is not empty
        current = queue.pop(0)
        print(current.value)

        if current.left is not None:  #add left child to the back of the queue, if none proceed to check from right
            queue.append(current.left)

        if current.right is not None: #add right child to the back of the queue
            queue.append(current.right)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

print(bfs(root))