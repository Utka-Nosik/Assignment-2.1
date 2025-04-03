class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.back = new_node
            self.head = new_node

    def middle(self):
        temp1 = self.head
        temp2 = self.head
        while temp2 and temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next.next
        print(temp1.data)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next
        print("None")

n = LinkedList()

k = list(map(int, input().split()))

for i in k:
    n.append(i)

n.display()
n.middle()
