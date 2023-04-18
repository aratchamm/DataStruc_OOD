class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)
  
class AVL_Tree: 
    #code here
    def insert(self, root, data):
        if root == None:
            root = Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
    
        root.height = max(self.getHeight(root.right), self.getHeight(root.left)) + 1
        balance = self.getBalance(root)

        # left left
        if balance > 1 and data < root.left.data:
            print("Not Balance")
            return self.rightR(root)
        
        elif balance < -1 and data >= root.right.data:
             print("Not Balance")
             return self.leftR(root)
        
        elif balance > 1 and data >= root.left.data:
             print("Not Balance")
             root.left= self.leftR(root.left)
             return self.leftR(root)

        elif balance < -1 and data < root.right.data:
             print("Not Balance")
             root.right = self.rightR(root.right)
             return self.rightR(root)

        return root

    def leftR(self,z):
        y = z.right
        temp = y.left
        y.left = z
        z.right = temp

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y

    def rightR(self,z):
        y = z.left
        temp = y.right
        y.right = z
        z.left = temp
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y



    def getHeight(self,root):
        if not root:
            return 0
        else:
            return root.height

    def getBalance(self,root):
        if not root:
            return 0
        else:
            return self.getHeight(root.left) - self.getHeight(root.right)


def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None
data = list(map(int,input("Enter Input : ").split()))
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")