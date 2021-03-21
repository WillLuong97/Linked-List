#Problem 25. Reverse Nodes in k-Group

'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
 

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
'''
#Definition of a linked list node: 
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None


#Function to print out a linked list 
def printList(head):
	current = head
	array = [] 
	while current:
		array.append(current.val)
		current = current.next
	return array	

def reverseKGroup(head, k):
	#an array of node to swap
	arrayOfSwappedNode = []
	current = head
	prev = None
	flag = False
	#going through the array to swap the list node
	while current:
		arrayOfSwappedNode.append(current) 
		nextNode = current.next
		current.next = None
		current = nextNode
	#if we cant reverse the list based on the k
	if len(arrayOfSwappedNode) < k:
		return head
	#loop through the list of node and reverse the node k times
	for i in range(1, len(arrayOfSwappedNode)):
		#if k has not yet been reached so keep reversing the 
		#contained element
		if i % k != 0:
			arrayOfSwappedNode[i].next = arrayOfSwappedNode[i-1]
		elif (i+k+1) < len(arrayOfSwappedNode):
			arrayOfSwappedNode[i-k].next = arrayOfSwappedNode[i+k-1]
		else: 
			#if the element K has been maxed out, then the last thing that we need to do is to reverse the first element in the array
			#with the current ones. 
			arrayOfSwappedNode[i-k].next = arrayOfSwappedNode[i]	
			flag = True
			break
	#if we are able to reverse the linked list, then convert the array back into the linked list and return it
	if flag: 
		for i in range(len(arrayOfSwappedNode) - len(arrayOfSwappedNode) % k, len(arrayOfSwappedNode) - 1):
			arrayOfSwappedNode[i].next = arrayOfSwappedNode[i+1]
	return arrayOfSwappedNode[k-1]


#Main function to run the test cases: 
def main():
	print("TESTING REVERSE NODES IN K-GROUP...")
	head = ListNode(1)
	two = ListNode(2)
	three = ListNode(3)
	four = ListNode(4)
	five = ListNode(5)
	k = 2
	print(reverseKGroup(head, k))
	

	print("END OF TESTING...")

main()
