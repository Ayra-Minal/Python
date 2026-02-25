class Node():
    def __init__(self, value):
        self.value=value
        self.next=None

class Linkedlist():
    def __init__(self):
        self.head=None 

    def insert_back(self,value):
        new1 = Node(value)
        if self.head is None:
            self.head = new1
            return self.head.value
        current=self.head
        while current.next:
            current=current.next
        current.next=new1    

    def insert_front(self,value):
        new=Node(value)
        new.next=self.head
        self.head=new

    def insert_after_k(self,value,k):
        new_node = Node(value)
        current = self.head
        if current is None:
            self.head = new_node
            return
        for i in range (k-1):
            if current.next is None:
                break
            current = current.next
        new_node.next=current.next
        current.next=new_node
    
    def delete_front(self):
        if self.head is None:
            return -1
        else:
            gone=self.head.value
            self.head=self.head.next
            return gone
        
    def delete_val(self,val):
        if self.head is None:
            return -1
        if self.head.value==val:
            self.head=self.head.next
            return
        else:
            current=self.head
            while current.next:
                if current.next.value==val:
                    current.next=current.next.next
                else:
                    current=current.next   
            return         

    def get_head(self):
        if self.head is None:
            return -1
        else:
            return self.head.value   

    def get_last_value(self):
        if self.head is None:
            return -1
        current = self.head
        while current.next:
            current = current.next
        return current.value         
    
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
'''
if __name__=="__main__":
    ll=Linkedlist()
    c=1
    while (c):
        n=int(input("enter value :"))
        ll.insert_front(n)
        print("continue? 1/0 ")
        c=int(input())
    head=ll.get_head()
    print("value at head is: ",head)
    print("entire linked list is:", ll.get_entire_val())
'''

        
