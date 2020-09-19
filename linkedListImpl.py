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
        while temp: 
            print(temp.value)
            temp = temp.next

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
main()