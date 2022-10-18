'''
นำ code จากข้อ 1 มาเปลี่ยนเป็น

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])

เพื่อหาว่าค่าแรกที่ใส่เข้าไปอยู่ที่ตำแหน่งใดใน BST

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while cur != None:
                if data >= cur.data:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    cur = cur.right
                elif data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    cur = cur.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self,data):
        cur = self.root
        while cur != None:
            if data == cur.data:
                if cur.data == self.root.data:
                    return print("Root")
                elif cur.left == None and cur.right == None:
                    return print("Leaf")
                else:
                    return print("Inner")
                    

            elif data < cur.data:
                if cur.left == None:
                    return print("Not exist")
                else:
                    cur = cur.left

            elif data > cur.data:
                if cur.right == None:
                    return print("Not exist")
                else:
                    cur = cur.right
     

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(T.root)
T.checkpos(inp[0])