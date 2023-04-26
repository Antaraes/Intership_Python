class Node:
    def __init__(self,data:dict):
        self.data= data
        self.left: Node = None
        self.right: Node = None

main_tree_data = []
for i in range(97, 123):
    main_tree_data.append(chr(i))

def insertion(alpha, root_tree :Node):
    if root_tree is None:
        return Node(alpha)
    if ord(alpha)<ord(root_tree.data):
        root_tree.left = insertion(alpha , root_tree.left)
    else:
        root_tree.right = insertion(alpha,root_tree.right)

    return root_tree

def printing(node):

    if node is not None:
        printing(node.left)
        print(node.data)
        printing(node.right)

length = len(main_tree_data)
mid = int(length/2)
tree = Node('m')

first_part = main_tree_data[0:mid-1]
sec_part = main_tree_data[mid:length]

first_part.reverse()
for i in range(len(first_part)):
    tree = insertion(first_part[i],tree)


for i in range(len(sec_part)):

    tree = insertion(sec_part[i],tree)

#printing(tree)

def get_tree():
    return tree




