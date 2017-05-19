class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        node.next = None
      
    def remove_index(self, index):
        prev = None
        node = self.head
        i=0
        while (node!=None) and (i<index):
            prev = node
            node = node.next
            i+=1
        if prev == None:
            self.head = node.next
        elif node.next == None:
            self.tail = node
        else:
            prev.next = node.next

    def remove_data(self, data):
        prev = None
        node = self.head
        found = False
        while node and found == False:
            if node.data == data:
                found = True
            else:
                prev = node
                node = node.next
        if prev == None:
            self.head = node.next
        elif node.next == None:
            self.tail = node
        else:
            prev.next = node.next
        
    def print_llist(self):
        node = self.head
        while node != None:
            print (node.data)
            node = node.next
