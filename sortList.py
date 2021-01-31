#Problem 148. Sort List
'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, val=0):
		 self.val = val
		 self.next = None

#Structure of the linked list: 	
class LinkedList: 	
	def __init__(self):
		self.head = None
	
	#function to add value into the linked list: 
	#insert to the back
	def append(self, val):
		#init a list node value from the new data
		new_node = ListNode(val)
		#if the list is empty, then the new node will be put into the 
		#head position
		if self.head is None: 
			self.head = new_node
			return
		current = self.head
		#looping through the rest of the linked list and append the value into the list
		while current.next is not None: 
			current = current.next
		#append the new node at the end of the linked list
		current.next = new_node
	#helper method to sort and merge the partitions of the linked list together
	def sortMerge(self,left, right):
		#base case:
		#result is a list node object
		result = None
		#the linekd list has been sorted as all partition has been put together into ones
		if left == None: 
			return right
		if right == None:
			return left

		
		#sort the partition(partition is a list node object)
		if left.val <= right.val:
			result = left
			result.next = self.sortMerge(left.next, right)

		else: 
			result = right
			result.next = self.sortMerge(left, right.next)
	
		return result
		
	#function to sort the linked list
	def sortList_RECURSION(self, head):
		#base case: 
		if head == None or head.next == None: 
			return head
		
		#get the middle value of the linked list: 
		midNode = self.getMiddleValue(head)
		#store the pointer after the mid value into halves
		afterMidNode = midNode.next
		midNode.next = None
		#split the linked list into equals part
		left_partition = self.sortList(head)
		right_partition = self.sortList(afterMidNode)
		#sort the and merge the partition together
		result = self.sortMerge(left_partition, right_partition)
		return result		
	
		
		
	#helper method to get the middle value of the min node
	def getMiddleValue(self, head):
		#base case:
		if not head: 
			return head
		#two pointers to find the mid value in the linked list
		#1->2->3->4
		slowPtr = head
		fastPtr = head

		while fastPtr.next != None and fastPtr.next.next != None:
			slowPtr = slowPtr.next
			fastPtr = fastPtr.next.next

		return slowPtr

	#Function to sort the linked list using merge sort iteratively
	def sortList_ITERATIVE(self, head):
		if not head or not head.next: return head

		def getSize(head):
			# Simply count the length of linked list
			counter = 0
			while head:
				counter +=1
				head = head.next
			return counter

		def split(head, size):
			# given the head & size, return the the start node of next chunk
			for i in range(size-1): 
				if not head: 
					break 
				head = head.next

			if not head: return None
			next_start, head.next = head.next, None  #disconnect
			
			return next_start

		def merge(l1, l2, dummy_start):
			# Given dummy_start, merge two lists, and return the tail of merged list
			curr = dummy_start
			while l1 and l2:
				if l1.val <= l2.val:
					curr.next, l1 = l1, l1.next
				else:
					curr.next, l2 = l2, l2.next
				curr = curr.next
			
			curr.next = l1 if l1 else l2
			while curr.next: curr = curr.next  # Find tail
			# the returned tail should be the "dummy_start" node of next chunk
			return curr  

		total_length = getSize(head)
		dummy = ListNode(0)
		dummy.next = head
		start, dummy_start, size = None, None, 1

		while size < total_length:
			dummy_start = dummy
			start = dummy.next 
			while start:
				left = start
				right = split(left, size) # start from left, cut with size=size
				start = split(right, size) # start from right, cut with size=size
				dummy_start = merge(left, right, dummy_start)  # returned tail = next dummy_start 
			size *= 2
		return dummy.next

#function to print out the list: 
def printList(head): 
	if not head: 
		return None

	current = head
	while current: 
		print(current.val)
		current = current.next
		

#Main function: 
# [4,2,1,3]
def main():
	print("TESTING SORT LIST...")
	llist = LinkedList()
	#creating a linked list: 
	llist.append(4)
	llist.append(2)
	llist.append(1)
	llist.append(3)

	llist.head = llist.sortList_ITERATIVE(llist.head)
	print("Sorted linked list is: ")
	printList(llist.head)
	print("END OF TESTING...")
main()
