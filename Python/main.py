datas = {}
class Node():
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.item

class LinkedList():
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.item)
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        name = input("name:")
        password = input("password:")
        key = len(node)
        if self.head.item.name == name:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

# if __name__ == '__main__':
#     linkedList = LinkedList()
#     linkedList.head = Node(1)
#     second = Node(2)
#     third = Node(3)
#     fouth = Node(4)
#
#     linkedList.head.next = second
#     second.next = third
#     third.next = fouth
#
#     while linkedList.head != None:
#         print(linkedList.head.item, end=" ")
#         linkedList.head = linkedList.head.next
if __name__ == '__main__':

    linked_list = LinkedList()
    stop = True
    while(stop == True):
        userInput = input("add or remove or print ")
        if(userInput == "add"):
            userAdd = input("type name ")

            linked_list.add_to_tail(Node(userAdd))
        elif(userInput == "remove"):
            linked_list.remove_from_head()
        elif(userInput == "print"):
            print("linked",linked_list)
            stop = False
# linked_list.add_to_tail(Node('john'))
# linked_list.add_to_tail(Node('sally'))
# print("ll:", linked_list)
# first = linked_list.remove_from_head()
# print("removed:", first)
# print("ll:", linked_list)