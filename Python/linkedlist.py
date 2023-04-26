class Node():
    def __init__(self, name, password, email, phone, age):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.age = age
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def add_data(self, name, password, email, phone, age):

        if self.head is None:
            self.head = Node(name, password, email, phone, age)
            return
        current = self.head 
        while current.next is not None:
            current = current.next
        if current.email != email:
            current.next = Node(name, password, email, phone, age)
        else:

            print("Email already exits. Input another email")

    def print_lists(self):
        current = self.head
        while current is not None:
            print({"name": current.name, "password": current.password, "email": current.email, "phone": current.phone,
                   "age": current.age})
            current = current.next


if __name__ == "__main__":
    linkedlist = LinkedList()
    stop = True
    while stop:
        userInput = input("add or print:")
        if userInput == "add":
            name = input("name:")
            password = input("password:")
            email = input("email:")
            age = input("age:")
            phone = input("phone:")
            linkedlist.add_data(name, password, email, phone, age)
        elif userInput == "print":
            linkedlist.print_lists()
            stop = False
