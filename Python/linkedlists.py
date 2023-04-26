class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            self.size += 1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)
            self.size += 1

    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next


def main():
    data = {0: {'name': 'min', 'password': 'min'}, 1: {'name': 'bhone', 'password': 'bhone'},
            2: {'name': 'thatn', 'password': 'thant'}}
    linkedList = LinkedList()
    for i in range(len(data)):
        name = input("Enter name: ")
        while name in [data[j]['name'] for j in range(i)]:
            print("Name already exists. Please enter a different name.")
            name = input("Enter name: ")
        password = input("Enter password: ")
        linkedList.add({'name': name, 'password': password})
    linkedList.printList()


if __name__ == "__main__":
    main()
