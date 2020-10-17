#Python3 code to design and implemnet a doubly linked list
#list node structure
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Linkedlist: 
    #constructor to build doubly linked list 
    def __init__(self):
        self.head = None

    #function to traverse the linked list and print out all element in an array forms
    #for debugging purposes
    def printNode(self):
        temp = self.head 
        #array to store all the element in the linked list 
        arrayOfNode = []
        while temp:
            arrayOfNode.append(temp.value)
            temp = temp.next

        return arrayOfNode

    #function insert element into the start of the list
    def insertIntoLinkedList(self, data):
        #if the linked list is empty: 
        if not self.head: 
            new_node = DoublyNode(data)
            #set the new data to the head values
            self.head = new_node
            return 

        #if the list is not empty: 
        new_node = DoublyNode(data)
        new_node.next = self.head
        self.head.previous = new_node
        #after the insertion, the new node will become the head of the linked list
        self.head = new_node
        

#function to create a deep copy of the doubly linked list
#Deep copy definition: 
'''
Deep copy of a Linked List means we do not copy the references of the nodes of the original Linked List rather for each node in the original Linked List a new node is created.
'''
#helper method to perform the recurisve copy of the doubly linked list
def recursiveCopy(head, prev_node):
    #base case: if the linked list is empty then return empty list
    if not head: 
        return None

    #create a new copy of the list node
    copied_node = DoublyNode(head.value)

    #copy the previous node of the current head value
    copied_node.prev = prev_node

    #copy the next node of the current head value
    copied_node.next = recursiveCopy(head.next, copied_node)

    return copied_node

#Function to create a deep copy of the doubly linked list
def deepCopy_DOUBLY(head):
    return recursiveCopy(head, None)

#function to traverse the linked list and print out all element in an array forms
#for debugging purposes
def printNode_New(head):
    temp = head 
    #array to store all the element in the linked list 
    arrayOfNode = []
    while temp:
        arrayOfNode.append(temp.value)
        temp = temp.next

    return arrayOfNode

#main function to test and execute the program
def main():
    print("***TESTING DOUBLY LINKED LIST IMPLMENTATION**********")
    #create an instance of a doubly linked list: 
    llist_doubly = Linkedlist()
    #add elememt into the linked list
    for i in range(11):
        llist_doubly.insertIntoLinkedList(i)
    print("Linked list created is: ")
    print(llist_doubly.printNode())

    print("A deep copy of the linked list is: ")
    deepLinkedList = deepCopy_DOUBLY(llist_doubly.head)
    print(printNode_New(deepLinkedList))
main()