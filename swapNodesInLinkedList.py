#Swapping nodes in a linked list

'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:

Input: head = [1], k = 1
Output: [1]
Example 4:

Input: head = [1,2], k = 1
Output: [2,1]
Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100

'''
#Definition for a singly linked list
class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

#function to solve the problem
def swapNodes(self, head, k):
        #base case: empty list, empty return value 
        if not head:
                return None
        #getting the total length of the linked list
        total  = 0 #1-indexed
        now = head
        #loop through the linked list to calculate the total length 
        while now:
            now = now.next
            total += 1
        #find the first and second kth node index
        k = min(k, total-k+1)
        #if both the first node and last node is the same value, the we do not need to swapp the values
        if k == total-k+1:
            return head

        #otherwise, loop through the linked list to find the two nodes and swapp them 
        current_node = head
        first_kth_node = head
        second_kth_node = head
        local_index = 1

        while local_index != total-k+1:
            current_node = current_node.next
            local_index += 1
            #finding the first node
            if local_index == k:
                    first_kth_node = current_node

            elif local_index == total-k+1:
                    second_kth_node = current_node

            
        #swapping the values 
        first_node_val_tmp = first_kth_node.val
        first_kth_node.val = second_kth_node.val
        second_kth_node.val = first_node_val_tmp

        return head
	

		


#Main function to run the test cases: 
def main():
	print("TESTING SWAPPING NODES IN A LINKED LIST...")

	#Test cases: 
	head = [1,2,3,4,5], k = 2
	head = [7,9,6,6,7,8,3,0,9,5], k = 5
	head = [1], k = 1
	head = [1,2], k = 1
	head = [1,2,3], k = 2


	print("END OF TESTING...")

main()

