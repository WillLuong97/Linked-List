#Problem 1670. Design Front Middle Back Queue
'''
Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:

FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
 
Example 1:
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
Constraints:
1 <= val <= 109

At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.


Appraoch using python3 built-in deque, which is a doubly linked list with efficient complexity of different operations. 
'''
#Creating my own deque using doubly linked list: 
#Definition of a doubly-linked-list node
class ListNode: 
	def __init__(self, val, prev = None, next = None):
		self.val = val 
		self.prev = prev
		self.next = next
	

#Defition of the front middle back queue: 
class FrontMiddleBackQueue:
	#init each value to be a doubly linked list node. 
	#init pointers to point at head, tail and middle of the queue
	def __init__(self): 
		self.head, self.tail, self.middle = None, None, None
		#variable to keep track of how many current elemnts are in the queue: 
		self.count = 0
	#Pushing element to the front of the queue
	def pushFront(self, val):
		#create a node from the target val:
		target_node = ListNode(val, None, self.head)
		#if the current list is empty, then we just put the element into it without much troubles:
		if not self.count:
			self.addFirstElement(val)
			return
		
		#otherwise, we will try to add it to the front
		self.head.prev = target_node 
		self.head = target_node	
		
		#keep track of the middle element, espeacially the most front middle element in the queue: 
		if self.count % 2 == 1: 
			self.middle = self.middle.prev
		
		self.count += 1
	
	def pushMiddle(self, val):
		pass

	#pusing the element to the back of the queue
	def pushBack(self, val):
		#if the current queue is empty so just simply put the target value into the queue: 
		if not self.count:
			self.addFirstElement(val) 
			return

		#creating a list node from the target value
		target_node = ListNode(val, self.tail, None)
		#connect the previous tail with the target_node:
		self.tail.next = target_node
		#override the tail node with the new target node: 
		self.tail = target_node
		#keep track of the middle element: when a new element is added to the queue from the front, the middle element will get pushed to the right 
		if self.count % 2 == 1: 
			self.middle = self.middle.next
	
		self.count += 1
		
	
	#popping element from the queue: 
	def popFront(self):
		#base case: 
		#case 1: empty queue: 
		if not self.count: 
			return -1 
 		#case 2: only 1 element to delete from the queue: 
		if self.count == 1: 
			return self.popFinalElement()		

		#node to be deleted: 
		node = self.head
		self.head = self.head.next
		self.head.prev = None

		#keeping track of the middle element: if an element is removed from the front, so the middle element will be 
		if self.count % 2 == 0: 
			self.middle = self.middle.next

		self.count -= 1
		return node.val
	
	#popping an element from the middle	
	def popMiddle(self):
		pass


	#popping element from the back
	def popBack(self):
		#base case: 
		#case 1: empty queue, nothing to pop, so return -1 
		if not self.count:
			return -1 
		if self.count == 1:
			return self.popFinalElement()
		
		#getting the node to be removed
		node = self.tail 
		self.tail = self.tail.prev
		self.tail.next = None
		#keeping track of the middle element, if the queue has only 1 middle element, then after removing a node from the back
		#then it will be the one on the leftmost
		if self.count % 2 == 1: 
			self.middle = self.middle.prev
		
		self.count -= 1
		return node.val  
			
			

	#helper method to push element to the queue if the queue is currently empty: 
	def addFirstElement(self, target):
		#Creatin a node structure of the target val:
		target_node = ListNode(target, None, None)
		#Increase the count by 1 as the list was replaced from empty to one value
		self.count = 1
		#point everything to this node
		self.head, self.tail, self.middle = target_node, target_node, target_node
	
	#helper method to the pop and return the only value in the current queue: 
	def popFinalElement(self):
		#Creating a new node ofthe target node
		target_node = self.head
		self.count = 0
		#point everything to the null, deleting the node value
		self.head, self.tail, self.middle = None, None, None
		return target_node.val
	
	#helper method to print all node value out from the queue for debugging:
	def printAllNode(self):
		array = []
		curr = self.head
		while curr: 
			array.append(curr.val)
			curr = curr.next

		return array





#Approach using deque import.
#from collections import deque
#class FrontMiddleBackQueue:
#	def __init__(self):
#		self.queue = []
#	
#	def pushFront(self, val):
#		#deque.insert(x, i)
#		#Insert x into the deque at position i.
#		self.queue.insert(0, val)
#
#	def pushMiddle(self, val):
#		#find the middle index of the queue and add the value to the at position
#		mid = len(self.queue) // 2
#		self.queue.insert(mid, val)
#	#use deuque.append, since append will all value to the right side of the queue
#	def pushBack(self, val): 
#		self.queue.append(val)
#
#	def popFront(self):
#		#if the queue is already empty so it will return -1
#		if len(self.queue) == 0:
#			return -1
#		return self.queue.pop(0)
#	
#	def popMiddle(self):
#		#Check if the array is empty or not: 
#		if len(self.queue) == 0:
#			return -1
#		#There will be two middle value if the len of the queue is even and 1 middle value if the length of the 
#		#queue is odd
#		if len(self.queue) % 2 == 0:
#			mid = len(self.queue) // 2
#			#decrement mid by one to get the leftmost mid index
#			mid -= 1
#			x = self.queue[mid]
#			#parse the queue into a new queue without the selected mid value
#			self.queue = self.queue[:mid] + self.queue[mid+1:]
#			return x
#
#		else: 
#			mid = len(self.queue) //2 
#			x = self.queue[mid]
#			self.queue = self.queue[:mid] +  self.queue[mid+1:]
#			return x	
#	
#	def popBack(self):
#		#Check to see if the arary is empty or not, if so, then return -1
#		if len(self.queue) == 0:
#			return -1
#		return self.queue.pop()
#Main function to run the test cases: 
def main():
	print("TESTING DESIGN FRONT MIDDLE BACK QUEUE...")
	q = FrontMiddleBackQueue()
	q.pushFront(1)   
	q.pushBack(2)   
	q.pushMiddle(3)  
	q.pushMiddle(4)
	print(q.printAllNode())
	q.popFront()     
	q.popMiddle()    
	q.popMiddle()    
	q.popBack()      
	q.popFront()     
			

	print("END OF TESTING...")


main()
