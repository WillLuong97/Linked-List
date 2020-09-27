#Python3 implementation of the leetcode problem 1367. Linked List in Binary Tree
#Problem statement: 
'''
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Example 1: 
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  

Example 2: 
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

Example 3: 
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.

'''
COUNT = [10]
#Set up the tree
class TreeNode: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Set up the list node
class ListNode: 
    def __init__(self, data):
        self.data = data
        self.next = None


#Set up the linked list: 
class LinkedList: 
    def __init__(self):
        self.head = None

    #function to print out the linked list
    def printNode(self):
        current = self.head

        while current: 
            print(current.data)
            current = current.next        

#Function to print out a binary tree in 2D
def print2D(root):
    print2DUtil(root, 0)

#helper method to assist with printing a tree out
def print2DUtil(root, space):
    #base case: if the tree is empty, there are nothing to print out
    if not root: 
        return

    #increase the space between cells
    space += COUNT[0]

    #Process the right child first
    print2DUtil(root.right, space)
    #print the current node after the space
    print()

    for i in range(COUNT[0], space):
        print(end=" ")

    print(root.data)

    #process the left child: 
    print2DUtil(root.left, space)

#Fucntion to check if a tree has a path to all the element in the linked list on a downward model
#We will use the breadth first search algorithm to traverse the tree
def isSubPath(head: ListNode, root: TreeNode) -> bool: 
    #base case: 
    if not head: 
        return True
    if not root: 
        return False

    #create a queue to store all element extracted from the tree using breadth first search
    q = [root]

    while q: 
        treeNode = q.pop(0)
        #check to see if the treenode we just popped is in the linked list path or not
        if matchNodes(head, treeNode):
            return True

        #repeat the above process if the current tree node has a left or a right subtree
        if treeNode.left: 
            q.append(treeNode.left)

        if treeNode.right: 
            q.append(treeNode.right)

    return False

#helper method to check if the tree node and the linked list node are matched or not
def matchNodes(head,root): 
    #base case: 
    if not head: 
        return True
    
    if not root: 
        return False

    #check to see if there is a path between the tree node and the linked list node
    if head.data != root.data: 
        return False

    return matchNodes(head.next, root.left) or matchNodes(head.next, root.right)



#Main function to execute the program: 
def main():
    print("TESTING CODE FOR Linked List in Binary Tree...")
    #create a linked list: 
    print("Linked list created: ")
    llist = LinkedList()

    #add node into the linked list
    llist.head = ListNode(4)

    second = ListNode(2)
    third = ListNode(8)
    llist.head.next = second
    second.next = third

    llist.printNode()
    #create a tree: 
    print("Binary tree created: ")
    # [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
    root = TreeNode(1)
    root.right = TreeNode(4)
    root.left = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(8)
    root.right.left.right.left = TreeNode(1)
    root.right.left.right.right = TreeNode(3)

    print2D(root)
    print(" ")
    print("TESTING is sub path...")
    print(isSubPath(llist.head, root))


    print("END OF TESTING...")
main()