#Problem 1290. Convert Binary Number in a Linked List to Integer
'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:
Input: head = [0,0]
Output: 0

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.

To convert a binary number into a decmial
ex: 101 = 1 * 2^2 + 0 * 2^1 + 1 * 2^0 => 5

1 -> 0 -> 1
curr.val = curr.val * 2 + curr.next.val
Approach: we will go through each element in the linked list and calculate each node based on the equation above.  
'''
#List node data model: 
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

def getDecimalValue(head):
	#base case:
	if not head: 
		return None
	curr_val = head.val 
	#loop through the linked list to find the element
	while head.next:
		curr_val = curr_val * 2 + head.next.val
		head = head.next
	return curr_val

#Time complexty: O(n), n is the number of all node in a linked list, because the algorithm has to look through all node val to construct the decimal number
#Space complexity: O(1)


#Main function to test the code: 
def main():
	print("TESTING CONVERT BINARY NUMBER IN A LINKED LIST TO DECIMAL...")
	head = ListNode(1)
	zero = ListNode(0)
	two = ListNode(1)
	head.next = zero
	zero.next = two
	print(getDecimalValue(head))
	print("END OF TESTING...")

main()


