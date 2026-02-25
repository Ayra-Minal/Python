class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class clinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self,value): 
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next=self.head    






'''
while True:
        print("\n--- Linked List Menu ---")
        print("1. Insert at front")
        print("2. Insert at back")
        print("3. Insert at position/middle")
        print("4. Delete a node of value")
        print("5. Delete front")
        print("5. Delete tail")
        print("6 Delete at index")
        print("5. View head")
        print("6. View entire list")
        print("7. Exit")
'''     
        
        