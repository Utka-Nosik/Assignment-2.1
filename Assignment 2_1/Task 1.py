class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete(self, data):
        temp = self.head
        if temp.data == data:
            self.head = temp.next
        while temp and temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                break
            temp = temp.next
    def search(self, data):
        m = False
        index = 1
        temp = self.head
        while temp:
            if temp.data == data:
                m = True
                break
            temp = temp.next
            index += 1
        if m:
            print('index of element:', index)
        else:
            print('element not found')

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

n = LinkedList()

k = list(map(int, input().split()))

for i in k:
    n.append(i)
choose = str(input('Choose action delete or search (D/S): '))
if choose == 'D':
    del_k = int(input('Delete element: '))
    n.delete(del_k)
if choose == 'S':
    ser_k = int(input('Search element: '))
    n.search(ser_k)
elif choose != 'D' and choose != 'S':
    print('Invalid input')

n.display()
