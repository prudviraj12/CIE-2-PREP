# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Create / Insert at End
    def create(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Display
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Insert at Beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at Position
    def insert_position(self, pos, data):

        if pos == 1:
            self.insert_begin(data)
            return

        new_node = Node(data)

        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


# Driver Code
ll = LinkedList()

ll.create(10)
ll.create(20)
ll.create(30)

print("Original List:")
ll.display()

ll.insert_begin(5)
print("After Insert at Beginning:")
ll.display()

ll.insert_end(40)
print("After Insert at End:")
ll.display()

ll.insert_position(3, 15)
print("After Insert at Position:")
ll.display()