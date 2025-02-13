class Node:
    def __init__(self,data):
        self.data = data
        self.next = None   #next node
        self.prev = None   #previous node
class doubly_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_tail(self,data):
        new_node = Node(data)
        if not self.head:  #here we check whether the list is empty
            self.head = new_node   #by this condition if head was empty means list is empty
            self.tail = new_node    #so in empty list head and tail is new node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def insert_head(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    def insert_index(self,index,data):
        new_node = Node(data)
        if index == 0:
            self.insert_head(data)
            return f"item is added."
        tmp = self.head
        count = 0
        while tmp and count < index - 1: #while the counter is not read to desire index -1
            tmp = tmp.next
            count +=1
        if not tmp: #for instance we have 4 item in list , then we want to add new data to index 8. counter start count from item with index 1 if exist it goes to next , then reach to item with index 4 then counter is equal to 5 the in the next node there is nothing(node), means the index is out of bound
            return f"indext{index} is out of bound"
        if tmp.next is None:  #if desired index was the index of the item in the last index (which prev pointer is equal to None)
            self.insert_tail(data)
            return f"item is added"
        new_node.next = tmp.next
        new_node.prev = tmp
        tmp.next.prev = new_node
        tmp.next = new_node
        
    def display_forward(self):
        forward = self.head
        print("------- table -------")
        headers = ["State/UTs", "Zone", "Total Cases", "Active", "Discharged", "Deaths",
               "Active Ratio", "Discharge Ratio", "Discharge Avg", "Death Ratio",
               "Death Avg", "Population"]
        print(", ".join(headers))
        print("\n")
        while forward: #if forward in not empty
            print(f"{forward.data}")
            forward = forward.next
        return f"None"
    def display_backward(self):
        back = self.tail
        while back:
            print(f"{back.data}")
            back = back.prev
        return f"None"
        


