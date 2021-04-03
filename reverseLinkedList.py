#Problem 206. Reverse Linked List

'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

#Definition to reverse a linked list:
class LinkedList:
	def __init__(self, val):
		self.val = val
		self.next = None
#ITERATIVE APPROACH: (Time complexity: O(n), space complexity: 0(1))
def reverseList(head):
	#check if the list is empty or not:
	if not head:
		return None
	#use two pointer, current for the current node and previous for previous node: 
	prev = None
	current = head
	#traverse the list and have current.next to point to previous node
	while current: 
		#store the original next node before the swap
		nextNode = current.next
		#reverse by having the current node to point to the previous node
		current.next = prev
		prev = current
		current = nextNode
	return prev

#RECURSIVE method: (Time complexity: O(n), space complexity: O(n))
def reverseList_RECURSIVE(head):
	if not head or not head.next:
		return head
	node = reverseList_RECURSIVE(head.next)
	head.next.next = head
	head.next = None
	return node


def printListNode(head):
	if not head:
		return []
	result = []
	current = head
	while current:
		result.append(current.val)
		current = current.next
	return result

#Main function to test the code:
def main():
	print("TESTING REVERSE A LINKED LIST...")

	head = LinkedList(1)
	two = LinkedList(2)
	three = LinkedList(3)
	four = LinkedList(4)
	five = LinkedList(5)
	head.next = two
	two.next = three
	four.next = five
	print("List before reverse: ")
	print(printListNode(head))	
	print("List after reverse: ")
	newList = reverseList(head)
	print(printListNode(newList))
	print("List after reverse with recursion: ")
	newList_2 = reverseList_RECURSIVE(head)
	print(printListNode(newList_2))
	
	print("END OF TESTING...")
main()


