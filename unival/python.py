class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def is_unival(self):
        if self.data == None:
            return True
        resultL = False
        resultR = False
        if(self.left == None or self.left.data == self.data):
            resultL = True
        if(self.right == None or self.right.data == self.data):
            resultR = True
        return resultL and resultR


count = 0


def countsame(root):
    global count
    if(root.is_unival()):
        count += 1

    if root.left != None:
        countsame(root.left)
    if root.right != None:
        countsame(root.right)

    return count


tree1 = Node(0)
tree2 = Node(0)
tree3 = Node(1)

tree1.left = Node(1)
tree1.right = tree2

tree2.left = tree3
tree2.right = Node(0)

tree3.left = Node(1)
tree3.right = Node(1)


print(countsame(tree1))
