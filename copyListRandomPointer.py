#python3 implementation of leetcode 138. Copy List with Random Pointer

#Problem statement:
'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
The number of nodes will not exceed 1000.
'''
#list node structure
class Node: 
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class SpecialLinkedList: 
    def __init__(self, head):
        self.head = None

    #function add element into the linked list: 
    def insertIntoLinkedList(self, data):
        #if the linked list is empty: 
        if not self.head: 
            new_node = Node(data)
            #set the new data to the head values
            self.head = new_node
            return 

        #if the list is not empty: 
        new_node = Node(data)
        new_node.next = self.head
        self.head.random = new_node.next.next
        #after the insertion, the new node will become the head of the linked list
        self.head = new_node

#function to make a deep copy of the current linked list with random pointer
def copyRandomList(head: 'Node') -> 'Node':
    #base case: 
    if not head:
        return None

    #visited dictionary to check if the current element has been repeated or not 
    visited = {}

    return recursivelyCopy(head, visited)

#helper method to recursively copy all element in the linked list
def recursivelyCopy(head, visited):
    #check if the head node has been visited or not
    if head in visited:
        return visited[head]

    #if not, then make a copy of the linked list andd assign it into the dictionary
    copiedNode = Node(head.val)

    visited[copiedNode] = head

    #the copied node would have next and random attribute from the class created: 
    #recursively call for the next and random element of the node
    copiedNode.next = recursivelyCopy(head.next, visited)
    copiedNode.randome = recursivelyCopy(head.random, visited)

    return copiedNode





    


        