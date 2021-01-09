#430. Flatten a Multilevel Doubly Linked List

'''
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 

Constraints:

The number of Nodes will not exceed 1000.
1 <= Node.val <= 105
'''
#List node object
class Node:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.next = None
		self.child = None

'''
   12  <-  current -> 32
'''
def flatten(head):
	#base case: 
	if not head: 
		return None
	
	stack = []
	current = head
	prev = None

	#traverse the linked list: 
	while current: 
		#check if the current node has a child list
		if current.child:
			#if current.next exist then we will store it onto the stack so that we can connect it again later
			if current.next:
				stack.append(current.next)
			
			#connect to the sublist by overring the next and prev attriubte of current node with its child node
			current.next, current.next.prev = current.child, current
		#when the sublist has been reached, we will connect to the original list by popping the element from the stack
		if not current.next and stack:
			current.next, current.next.prev = stack.pop(), current
		
		#continue to traverse the main list: 
		prev, current.child, current = current, None, current.next
	return head

'''
Time complexity: O(n), where n is every node in the linked list, including the sublist
Space complexity: O(1), we only have to store on the stack the next element of the node that contains the child node. 
'''
				
#Main function to run the test cases: 
def main():
	print("TESTING FLATTEN MULTLEVEL DOUBLY LINKED LIST...")
	#create a linkd list: 
	head = Node(1)
	head.next = Node(2)
	head.next.prev = head
	head.child = Node(3)
	print(flatten(head))
	print("END OF TESTING...")

main()




