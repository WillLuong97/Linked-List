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
from collections import deque
class FrontMiddleBackQueue:
	def __init__(self):
		self.queue = []
	
	def pushFront(self, val):
		#deque.insert(x, i)
		#Insert x into the deque at position i.
		self.queue.insert(0, val)

	def pushMiddle(self, val):
		#find the middle index of the queue and add the value to the at position
		mid = len(self.queue) // 2
		self.queue.insert(mid, val)
	#use deuque.append, since append will all value to the right side of the queue
	def pushBack(self, val): 
		self.queue.append(val)

	def popFront(self):
		#if the queue is already empty so it will return -1
		if len(self.queue) == 0:
			return -1
		return self.queue.pop(0)
	
	def popMiddle(self):
		#Check if the array is empty or not: 
		if len(self.queue) == 0:
			return -1
		#There will be two middle value if the len of the queue is even and 1 middle value if the length of the 
		#queue is odd
		if len(self.queue) % 2 == 0:
			mid = len(self.queue) // 2
			#decrement mid by one to get the leftmost mid index
			mid -= 1
			x = self.queue[mid]
			#parse the queue into a new queue without the selected mid value
			self.queue = self.queue[:mid] + self.queue[mid+1:]
			return x

		else: 
			mid = len(self.queue) //2 
			x = self.queue[mid]
			self.queue = self.queue[:mid] +  self.queue[mid+1:]
			return x	
	
	def popBack(self):
		#Check to see if the arary is empty or not, if so, then return -1
		if len(self.queue) == 0:
			return -1
		return self.queue.pop()
#Main function to run the test cases: 
def main():
	print("TESTING DESIGN FRONT MIDDLE BACK QUEUE...")
	q = FrontMiddleBackQueue()
	q.pushFront(1);   
	q.pushBack(2);   
	q.pushMiddle(3);  
	q.pushMiddle(4);
	q.popFront();     
	q.popMiddle();    
	q.popMiddle();    
	q.popBack();      
	q.popFront();     
			

	print("END OF TESTING...")


main()
