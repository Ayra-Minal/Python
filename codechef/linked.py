#linked in python
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
head=Node(1)
second=Node(2)
head.next=second
print(head.value)
print(head.next.value)
print(second.value)