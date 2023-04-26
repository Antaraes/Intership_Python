class ThirdNode:
    def __init__(self, data=None, se=None):
        self.data = data
        self.se = se
        self.left = None
        self.right = None

def third_insertion(data, se, root_tree):
    print(data)
    if root_tree is None:
        return ThirdNode(data, se)
    if se < root_tree.se:
        print("left")
        root_tree.left = third_insertion(data, se, root_tree.left)
    else:
        print("right")
        root_tree.right = third_insertion(data, se, root_tree.right)
    return root_tree

def printing(node):

    if node is not None:
        printing(node.left)
        print(node.data)
        printing(node.right)

# printing(tree)
# def get_tree():
#     return tree
