from dataclasses import dataclass


class Node():

    def __init__(self,data):
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)

def createList(lst=[]):
    head = Node(lst[0])
    cur = head
    for i in range(len(lst)):
        nxt = Node(lst[i])
        cur.next = nxt
        cur = cur.next
    return head


def printList():
    pass

def mergeOrderList():
    pass

