class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
     	self.left_tag = 1
     	self.right_tag = 1

if __name__ == "__main__":
	queue = []
	counter = 0
	root = Node(10) 
	root.left     = Node(7) 
	root.right     = Node(25) 
	root.left.left = Node(5) 
	root.left.right = Node(8) 
	root.right.right = Node(30)


def printInorder(root,queue): 
    if root: 
        # Recursion on left child
        printInorder(root.left,queue)
# Printing the data of the node
        print(root.val)
        queue.append(root)
# Recursion on the right child
        printInorder(root.right,queue)


def createThreadedTree(root,queue,counter):
    if root == None:
        return
    if root.left is not None:
        createThreadedTree(root.left,queue,counter)
        counter += 1
    else:
        # Added left tag
        root.left_tag = 0
        
        if counter == 0:
            root.left = None
        else:
            node = queue.pop(0)
            root.left = node
    if root.right is not None:
        createThreadedTree(root.right,queue,counter)
    else:
        node = queue.pop(0)
        
        # Added Right Tag
        root.right_tag = 0
        
        if len(queue) > 0:
            root.right = queue[0]
        else:
            root.right = None

def inorderThreadedTree(root):
    node = root
    #This is to go the leftmost node of the tree
    while(node.left):
        node = node.left
    
    #this is to check for all nodes
    while(node is not None):
        # if the left pointers of the nodes pointing to parent node 
        # then print the value and go to the 
        # right node (parent node). 
        # This is identified using left_tag 
        # (0 means poiting to parent node)
        if node.left_tag == 0:
            print(node.val)
            node = node.right
        else:
            print(node.val)
            node = node.right
            # if pointing to child node then keep on moving to child
            # left node
            if node and node.left_tag == 1:
                node = node.left

