#Python3 program to implement a linked list structure
#List Node structure 
class Node:
    #Function to initialize the node object
    def __init__(self, value):
        self.value = value  #Assign data
        self.next = None    #Initialize the next data as null
#Linked list structure
class LinkedLst:
    #function initialize a head node
    #Head node is often empty the linked list at this point has not been created yet
    def __init__(self):
        self.head = None

    #Fucntion to traverse a linked list and print out each element in the linked list
    def printNode(self):
        temp = self.head
        listNode = []
        while temp: 
            listNode.append(temp.value)
            temp = temp.next
        print(listNode) 
    #Function to reverse a linked list
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6
    #Output: 6 -> 10 -> 4 -> 3 -> 2 -> 1
    def reverseList(self):
        #the current element that we look at
        current = self.head
        #previous node to look at
        prev = None

        #looping through the linked list
        while current: 
            #getting the next node of the current node
            nextNode = current.next
            #setting the next node of the current to be the previous node (pointing the arrow backward)
            current.next = prev
            #move up in the linked lsit
            #let the previous node be the current node
            prev = current
            #current node to be the next node.
            current = nextNode
        #adding the reversed node into the tree. 
        self.head = prev

    #Function to delete a node in the linked list: 
    #The function will recieve a node value that needed to be deleted and then delete that node out of the linked list
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6 ,val = 10
    #Time complexity: Best case: O(1) if the head of the list or tail of the list is the node to be removed, this way, the deletion could happen immediately without the traversal.
                    #Average case: O(n) if the element to be removed is inside the list, so we will have to loop through the linked, with n being the length of the list. Worse case: O(n)
    #Output: 1 -> 2 -> 3 -> 4 -> 6
    def removeNode(self, val):
        #base case: 
        if not val: 
            return self.head.next

        #create a dummy node to look at all the previous element of a current node
        prev = Node(0)

        #conenct this dummy node to linekd list
        prev.next = self.head
        #traverse through the linked list and look for the element that we tries to remove
        while prev.next:
            if prev.next.value == val:
                prev.next = prev.next.next
            else: 
                prev = prev.next

        return self.head.next

    #Function to remove a group of node that are in a list in a linked list
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6 ,val = [1,2,3]
    #Output: 4 -> 10 -> 6 
    def removeGroupNode(self, nodes):
        #base case: 
        if not nodes:
            return self.head.next 
        
        #Dummy node to store the value that are previous to the current element
        previous = Node(0)
        #Connect the dummy node to the linked list
        previous.next = self.head
        #traverse through the linked list and look for any elements that are contained in the node
        while previous.next: 
            #if the next node of the dummy node is contained in the array, we will remove it
            if previous.next.value in nodes: 
                previous.next = previous.next.next
            #skip it and move to the next node
            else: 
                previous  = previous.next

        return self.head.next

    #Function to insert a node into the linked list: (Insertion into the tail)
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6, target = 5
    #Output: 1 -> 2 -> 3 -> 4 -> 10 -> 6 -> 5
    #Time complexity: O(n) with n being the length of the linked list, we will always have to go through the end of the list to add the target elemenet into
    def insertNode_LAST(self, target):
        #Base case: if there is no target to pass element in, then just return the current linked list
        if not target: 
            return self.head.next

        #create an instance of the Node object to pass in the target
        target_node = Node(target)
        #base case: if the list is empty, we will add the target value into the head. 
        if self.head is None:
             self.head = target_node
        #intialize a dummy node to look at each element in the linked list
        current = self.head
        #loop throught the linked list and add the target value into the linked list. 
        while current:
            if current.next == None: 
                current.next = target_node
                target_node.next = None
            current = current.next
        return current

    #Function to insert a node into a linked list: (Insertion into the head)
    #Input: 1 -> 2 -> 3 -> 4 -> 10 -> 6, target = 5
    #Output: 5 -> 1 -> 2 -> 3 -> 4 -> 10 -> 6
    #Time complexity: O(1), this is a constant time operation since we only have to reference the head node and add element into it
    def insertNode_HEAD(self, target):
        #base case: if there is no target to insert
        if not target: 
            return self.head.next
        target_node = Node(target)
        #base case: if the linked list is empty, and the head node is Null
        if self.head is None: 
            self.head = target_node
        
        currentHead = self.head
        self.head = target_node
        self.head.next = currentHead
        
        return self.head.next

            
# #Funtion to insert a node into a linked list after a given value: 
# def insertNode_GIVEN(self,target, position):
#     pass

#Function to return a deep copy of a single linked list
#Deep copy definition: 
'''
Deep copy of a Linked List means we do not copy the references of the nodes of the original Linked List rather for each node in the original Linked List a new node is created.
'''
def copy_list_SINGLY(head):
    #base case: if the linked list is empty, just return nothing
    if not head: 
        return head
    
    #Create a new node from the list node that was passed in
    copiedNode = Node(head.value)

    #set the newly created node to point to the next node that would be recursively created as a new node in the deep copy list
    copiedNode.next = copy_list_SINGLY(head.next)
    

    return copiedNode



#function to print out element from a linked list
def printNode_NEW(head):
    #base case: the linked list is empty
    if not head: 
        return None
    
    temp = head
    #list to store all the the node:
    linkedList = []
    while temp: 
        linkedList.append(temp.value)
        temp = temp.next

    return linkedList


#143. Reorder List: 

#Problem statement: 
'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
#Function to reorder a linked list: 
#2 pointer approach: 
def reorderList(head: Node) -> None: 
    #Pointer to access element in the linked list
    fastPtr = head
    slowPtr = head

    #get to the mid element
    while fastPtr and fastPtr.next:
        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next

    reverse = None
    #reverse element from mid to the last list node element:
    while slowPtr: 
        curr = slowPtr
        slowPtr = slowPtr.next
        curr.next = reverse
        reverse = curr
    
    #temporary head pointer to look at each list node element from the beginning
    tmpHeadPoitner = head
    revPtr = reverse

    #Loop through the linked list from the beginning and mix the first half with the element from the second half
    while tmpHeadPoitner:
        tmp = tmpHeadPoitner.next
        tmpHeadPoitner.next = revPtr
        revPtr = tmp
        tmpHeadPoitner = tmpHeadPoitner.next

#Problem 876. Middle of the linked list:

#problem statement: 
'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.
'''
#Solution function: 2 pointer approach
#Time complexity: O(N/2) -> O(n) where n is the number of node in a linked list.  
def middleNode(head: Node) -> Node:
    #base case: the linked list is empty
    if not head: 
        return None

    #create pointer to access the element
    slowPtr = head
    fastPtr = head

    while fastPtr and fastPtr.next:
        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next
        

    return slowPtr

#1290. Convert Binary Number in a Linked List to Integer
#Problem statement: 

'''
1290. Convert Binary Number in a Linked List to Integer
Easy

675

49

Add to List

Share
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
'''
def getDecimalValue(head: Node) -> int:
    #result value: 
    decimalValue = 0
    #reverse the linked list
    current = head
    prev = None
    
    #loop through the linked list and reverse it
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    #ovewrting the linked list with its reversed function
    head = prev
    #loop through the reversed linked list and start converting to the decimal value
    expo = 0
    while head:
        
        decimalValue += head.value * (2 ** expo)
        expo += 1
        head = head.next
    return decimalValue

#Time complexity: O(n), where n is the number of node in the binary linked list. The reversing of the lineked list would cost O(n) and the calculation would also cost O(n).
#In total: the time complexity would be O(n) + O(n) = O(n)
#Space complexity: O(1), we modify the string in place, so no need for extra memory allocation


#Leetcode 817. Linked List Components

'''
We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:

Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note:

If N is the length of the linked list given by head, 1 <= N <= 10000.
The value of each node in the linked list will be in the range [0, N - 1].
1 <= G.length <= 10000.
G is a subset of all values in the linked list.
'''
#The idea is to count the number of the connected component in a linked list by checking if the current node value is the tails of the connected component or not
#Loop through the linked list and check for the connected compoenent can be found in the G array
def numComponents(head, G):
    #base case: 
    if not head: 
        return None
    if len(G) == 0: 
        return None

    answer = 0
    Gset = set(G)

    current = head
    while current: 
        if current.value in Gset and (not current.next or current.next.value not in Gset): 
            answer += 1
        
        current = current.next

    return answer

#Leetcode 328. Odd Even Linked List
'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
'''
def oddEvenList(head):
    #base case: 
    if not head: 
        return None
    odd = head
    even = head.next
    even_head = even
    #loop through the original linked list construct the two sub linked list
    while even and even.next:
        #Constructing the two new linked list 
        odd.next = even.next 
        odd = odd.next
        even.next = odd.next
        even = even.next

    #Appending the even to the tail of the odd list
    odd.next = even_head

    return head
#Time complexity: O(n), where n is the length of the linked list
#Space complexity: O(1), we only need to store the pointer each time.





#Main function to creaete list node
def main():
    print("Linked List Implementation")
    print("")
    #create a linked list by creating an instance of class linked list
    llist = LinkedLst()
    #The first node is also the head node
    llist.head = Node(1)
    #the second node and the third node
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    five = Node(10)
    six = Node(5)
    #adding element into a linked list
    llist.head.next = second
    second.next = third
    third.next = forth
    forth.next = five
    five.next = six
    print("Created singly linked list is below: ")
    llist.printNode()

    print("")
    print("Reversing a linked list")
    llist.reverseList()
    llist.printNode()

    print("")
    print("Node Deletion")
    llist.removeNode(None)
    llist.printNode()
    print("")
    print("Remove node that are in a list of node.")
    nodes = [1,2,3]
    llist.removeGroupNode(nodes)
    llist.printNode()
    print("Insert Node Into The End of The List...")
    target = 6
    target_NULL = None
    target_12 = 12
    
    llist.insertNode_LAST(target)
    llist.printNode()
    llist.insertNode_LAST(target_NULL)
    llist.printNode()
    llist.insertNode_LAST(target_12)
    llist.printNode()
    print("Insert Node Into Head Of The List...")
    headTarget = 7
    emptyLL = LinkedLst()
    emptyLL.head = None
    emptyLL.insertNode_LAST(target)
    emptyLL.printNode()
    llist.insertNode_HEAD(headTarget)
    emptyLL.insertNode_HEAD(headTarget)
    llist.printNode()
    emptyLL.printNode()
    print("")
    print("Deep Copy a linked list: ")
    print("Original linked list: ")
    llist.printNode()
    newList = copy_list_SINGLY(llist.head)
    print("Deep copy version of the list: ")
    print(printNode_NEW(newList))
    print("Returning the middle element in the linked list: ")
    print(middleNode(llist.head))
    print("Converting binary number into decimal from linked list: ")
    binaryList = LinkedLst()
    binaryList.head = Node(1)
    binaryList.head.next = Node(0)
    binaryList.head.next.next = Node(1)
    print("Binary Linked List found: ")
    binaryList.printNode()
    print(getDecimalValue(binaryList.head))
    print("TESTING Linked List Components...")
    G = [0, 1, 3]
    linkedLst = LinkedLst()
    second_node = Node(0)
    third_node = Node(1)
    forth_node = Node(2)
    fifth_node = Node(3)
    linkedLst.head = second_node
    linkedLst.head.next = third_node
    third.next = forth_node
    forth.next = fifth_node
    print(numComponents(linkedLst.head, G))
    print("End of Program...")

    print(oddEvenList(linkedLst.head))

main()
