class Node:
    def __init__(self,data):
        self.data = data
        self.next = None   #next node
        self.prev = None   #previous node
class doubly_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_head(self,data):
        new_node = Node(data)
        if not self.head:  #here we check whether the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.head.next = new_node
            
