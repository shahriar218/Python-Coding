# A simple Python program for traversal of a linked list

class Node:


	def __init__(self, data):
		self.data = data
		self.next = None




class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None


	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next



if __name__=='__main__':

	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second;
	second.next = third;

	llist.printList()
