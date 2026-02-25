# linked insertion at end and return the last value everytime
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            return self.head.value
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    

    def get_entire_val(self):
        if self.head is None:
            return -1
        else:
            current=self.head
            values = []
            while current:
                values.append(current.value)
                current = current.next
            return values
        
    def get_last_value(self):
        
        if self.head is None:
            return -1
        
        current = self.head
        while current.next:
            current = current.next
        return current.value

if __name__ == "__main__":
    n = int(input("enter n"))
    linked_list = LinkedList()
    print("enter values")
    vals = list(map(int, input().split()))
    for x in vals:
        linked_list.insert_at_end(x)
        print(linked_list.get_last_value())
    print("deleted 5 from front  :",linked_list.delete_val(5))    
    print("entire linked list is:", linked_list.get_entire_val())    