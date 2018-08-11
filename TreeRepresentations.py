#Regular Tree
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

#Binary Tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None