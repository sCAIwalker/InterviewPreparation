from collections import deque

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#Recursive Solution
def createListOfDepths(root, listOfLinkedLists, level):
    if (root == None):
        return

    aList = []
    if (len(listOfLinkedLists) == level):
        listOfLinkedLists.append(aList.append(root.data))
    else:
        listOfLinkedLists[level].append(root.data)
    
    listOfDepths(root.left, listOfLinkedLists, level + 1)
    listOfDepths(root.right, listOfLinkedLists, level + 1)

def listOfDepths(root):
    listOfLinkedLists = []
    createListOfDepths(root, listOfLinkedLists, 0)
    return listOfLinkedLists

#Iterative Solution
def listOfDepths(root):
    if (root == None):
        return []

    queue = deque()
    queue.append(root)
    listOfLinkedLists = [[root.data]]
    while (len(queue) > 0):
        newQueue = deque()

        for node in queue:
            if node.left != None:
                newQueue.append(node.left)

            if node.right != None:
                newQueue.append(node.right)

        if len(newQueue) > 0:
            listOfLinkedLists.append([x.data for x in newQueue])

        queue = newQueue

    return listOfLinkedLists

