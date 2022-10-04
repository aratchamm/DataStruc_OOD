class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
    
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        s=''
        