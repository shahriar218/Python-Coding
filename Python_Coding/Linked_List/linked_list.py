# linear data structure
class Node:
    def __int__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __int__(self):
        self.head = None


# let's create a simple linked list with 3 node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

if __name__=='__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second;

	second.next = third;
