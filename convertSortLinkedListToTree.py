#Python3 implementation of leetcode 109. Convert Sorted List to Binary Search Tree

#Problem statement: 

'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
'''
#node structure
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
#Tree node structure
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Function to convert a Linked list into a binary search tree
def sortedListToBST_RECURSION(head):
        #base case: 
        if not head: 
            return None
        
        #getting the root node
        mid = getMidFromLinkedList(head)
        
        #Make the mid element to become the root of the tree
        root = TreeNode(mid.val)
        #base case: if the head is the mid, then just return node since the linked list only has 1 element in it
        if head == mid: 
            return root


        #recursively build the tree from the left and right side
        #the left sub tree would be from the head node to the mid element
        root.left = sortedListToBST(head)
        root.right = sortedListToBST(mid.next)
        
        return root
    
def getMidFromLinkedList(node):
    #initialize the pointers: 
    fastPTR = node
    slowPTR = node
    #dummy node to keep track of the previous elemet
    prev = None
    
    while fastPTR and fastPTR.next: 
        prev = slowPTR
        fastPTR = fastPTR.next.next
        slowPTR = slowPTR.next
    
    #if the slowPTR or the mid is equal to the head
    if prev: 
        prev.next = None
        
    return slowPTR


#Main progoram to run execute and test the function
def main():
    print("TESTING SORTED LINKED LIST TO BINARY TREE CONVERSION...")
    head = 2
    print("END OF TESTING")
main()