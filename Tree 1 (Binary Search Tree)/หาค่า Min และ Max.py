'''
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยและมากที่สุดของ Binary Search Tree

***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()
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


    def min(self, data):
        global min
        if(data < min):
            min = data
        return min

    def max(self, data):
        global max
        if(data > max):
            max = data
        return max

T = BST()
min = 99999
max = -99999
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    T.min(i)
    T.max(i)

T.printTree(T.root)
print("--------------------------------------------------")
print(f"Min : {min}")
print(f"Max : {max}")