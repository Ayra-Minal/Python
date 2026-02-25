class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_after_k(self,value:int,k:int):
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


if __name__=="__main__":
    n=int(input("number of val"))
    x,k=map(int,input("enter x and k").split())
    ll=Linkedlist()
    vals=list(map(int,input("enter values already in list").split()))
    for i in range (len(vals)):
        a=vals[i]
        ll.insert_after_k(a,i)
    ll.insert_after_k(x,k)
    print("entire linked list is:", ll.get_entire_val())            