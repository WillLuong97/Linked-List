#Problem: 1171. Remove Zero Sum Consecutive Nodes from Linked List

'''
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.

'''
#Deinfintion for singly linked list
class ListNode:
	def __init__(self, val=0):
		self.val = val
		self.next = None


#Function to find the zero sum consecutive nodes from the linked list
#Return type: head
def removeZeroSumSublists(head):
	#base case:
	if not head: 
		return head

	#Setting up the dummy node: 
	pointer = ListNode(float("inf"))
	#set the pointer to head node, this will be what we return at the end, this helps to keep track of the node that the head value looked at in the 
	#linked list
	pointer.next = head
	curr = head
	head = pointer
	#Looking at the linked list from the outer loop
	while head:
		current_sum = 0 
		while curr:
			#add the current value into the sum.
			current_sum += curr.val
			#if the sum is 0, delete all the consecutive node leading up to this node
			if current_sum == 0:
				head.next = curr.next
			#otherwise, keep looking at all the other nodes
			curr = curr.next
		#increment the outer loop if all the current inner loop through the linked list return no zero sum, then we keep checking
		head = head.next
		
		#if the outer loop still has element then we keep running the innner loop
		if head:
			curr = head.next

	return pointer.next

#Time complexity: O(n^2), we have the inner and outer loop to go through a linked list, which would give us a complexity of n^2 
#Space complexity: O(1)

#to string method to print out the linked list in array form
def toString(head):
	curr = head
	result = []
	while curr:
		result.append(curr.val)
		curr = curr.next
	
	return result
#Main function to run the test cases: 
def main():
	print("TESTING REMOVE ZERO SUM CONSECUTIVE NODES FROM LINKED LIST...")
	
	#test case: 
	head = ListNode(1)
	two = ListNode(2)
	three = ListNode(3)
	negThree = ListNode(-3)	
	one = ListNode(1)
	head.next = two
	two.next = negThree
	negThree.next = three
	three.next = one
	zeroSumTest = removeZeroSumSublists(head)
	print(toString(zeroSumTest))

	print("END OF TESTING...")


main()
