#Problem 445. Add Two Numbers II
'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''
#Defition for a singly linked list
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None


def addTwoNumbers(l1, l2):
	#string to store each node value and then use it to convert it into the integer
	s1 = ""
	s2 = ""
	int1 = 0
	int2 = 0
	#loop through each linked list and copy its value into a string
	curr1, curr2 = l1, l2
	#loop through the first linked list
	while curr1:
		s1 += str(curr1.val)
		curr1 = curr1.next
	
	#loop through the second linked list
	while curr2:
		s2 += str(curr2.val)
		curr2 = curr2.next
	
	#converting the two strings into two integers
	int1 = int(s1)
	int2 = int(s2)
	resSum = int1 + int2
	#convert the sum into a string so that we can loop over it add it into a new linked list
	strSum = str(resSum)
	#list 3 head
	l3 = ListNode(0)
	curr3 = l3
	for i in strSum:
		curr3.next = ListNode(int(i))
		curr3 = curr3.next

	return l3.next

def printAList(head):
	#result array
	result = []
	while head:
		result.append(head.val)
		head = head.next

	return result 
		 
		
#Main function to run the test cases: 
def main():
	print("TESTING ADD TWO NUMBERS II...")
	#test cases: 
	l1 = ListNode(7)
	l1.next = ListNode(2)
	l1.next.next = ListNode(4)
	l1.next.next.next = ListNode(3)

	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)

	l3 = addTwoNumbers(l1, l2)

	print("TEST CASES: ")
	print(printAList(l1))
	print(printAList(l2))

	print("RESULT: ")
	print(printAList(l3))


	print("END OF TESTING...")
main()
