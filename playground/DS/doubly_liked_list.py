class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # def delete(self, node):
    #     if node is None:
    #         return
    #
    #     if node == self.head:
    #         self.head = self.head.next
    #         if self.head:
    #             self.head.prev = None
    #         if node == self.tail:
    #             self.tail = None
    #         return
    #
    #     if node == self.tail:
    #         self.tail = self.tail.prev
    #         if self.tail:
    #             self.tail.next = None
    #         return
    #
    #     node.prev.next = node.next
    #     node.next.prev = node.prev

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':
    doublyLinkedList = DoublyLinkedList()

    doublyLinkedList.append(1)
    doublyLinkedList.append(2)
    doublyLinkedList.append(3)
    doublyLinkedList.append(4)

    doublyLinkedList.prepend(5)
    doublyLinkedList.prepend(6)

    doublyLinkedList.append(7)

    doublyLinkedList.print_list()

    # doublyLinkedList.delete(Node(6))

    doublyLinkedList.print_list()
